'''
项目管理

有 n 个项目，每个项目或者不属于任何小组，或者属于 m 个小组之一。group[i] 表示第 i 个项目所属的小组，如果第 i 个项目不属于任何小组，则 group[i] 等于 -1。
 项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

同一小组的项目，排序后在列表中彼此相邻。
项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。

 

示例 1：



输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]
示例 2：

输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
输出：[]
解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
 

提示：

1 <= m <= n <= 3 * 10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] 不含重复元素
'''
from typing import List
'''
思路：拓扑排序
从题目中知道：组内元素必须相邻。
所以需要进行2次拓扑排序：1次是组间的拓扑排序，排出各个组的顺序；第2次是组内的拓扑排序
TODO

先理解题意：
有 nn 个任务，每个题目可能属于 mm 个组中的一个（有的任务不属于任意一组，有的组没有任务）。
任务之间存在前驱关系，必须要完成所有前驱任务，才能完成对应的任务。
需要输出任务的安排顺序，要求前驱任务必须优先完成，同一组的任务必须相邻。

如果不考虑同一组任务必须相邻，那么看到要完成的任务之间存在前驱关系，应该想到 拓扑排序。

但是这里存在一个较为特别的要求：同一组的任务必须相邻。
考虑到如果有解，那么两个不同的组的任务，必然不可以存在交叉的前驱关系，也即小组 11 拥有任务 aa、bb，小组 22 拥有任务 cc、dd，
则不可能存在类似
aarr ca→c、d arr bd→b 的前驱关系。
所以，我们可以根据小组任务之间的前驱关系计算 小组之间的前驱关系。这样只需要按照得到的结果，分别对每个小组内部的任务进行拓扑排序后连接起来即可。

也即，整体思路如下：

计算小组之间的前驱关系
计算小组之间的拓扑排序
按照小组拓扑排序顺序分别计算组内拓扑排序
连接各组内拓扑排序结果
由于任务之间的前驱关系包含两种形式：前驱任务为其他组的任务、前驱任务为组内的前驱。前者在第 22 步排序，而后者在第 33 步排序，故结果必然正确。

这道题的另一个重点在于，数据量比较大，因此需要着重考虑性能优化。

可以考虑的点有以下几条：

拓扑排序不需要使用前驱数组，只需要入度数组即可，因为每个节点必然只会访问一次
和 11 的原因相同，在计算不同组的拓扑排序时，也不会修改其他组的入度，因此可以一次生成所有的入度、后驱数组
对于没有分配到组的任务，可以认为每个认为这些任务被分到一个只有一个任务的新组，可以直接在预处理阶段将起转换为全部都被分配的形式
所有可以在循环外的预处理，应该尽可能保持在循环外部进行
如果发现无法成功排序，应该及时结束程序。同时存在本身小组就未被分配任务的情况，应该识别出两种的不同
附上拓扑排序的大致思路:

预计算所有节点的入度（前驱数量）和后驱数组
找出所有入度为 00 的节点，插入到队列
如果队列非空，则取出一个节点：
将当前节点插入结果数组
将该节点的后驱节点的所有入度减一
如果其后驱节点入度为 00，则插入队列
重复上述过程
相当于每次都找一个没有前驱的节点插入结果，然后更新所有以该节点为前驱的节点。

这道题目的难点主要有两部分，一是针对组间拓扑关系的理解，一般而言应该可以想到这道题和拓扑排序有关，
但是如何将“相同组任务必须相邻”转换为拓扑排序并不是那么直观；
二是性能优化，由于要进行多次拓扑排序，因此涉及的数据很多，如何更快地完成数据预处理对是否超时至关重要。

import queue

class Solution:
    def topSort(self, nodes, indgree, suffix):
        # print(nodes, indgree, suffix)
        n = len(nodes)
        q = queue.Queue()
        res = []

        # 插入入度为 0 的点
        for i in nodes:
            if indgree[i] == 0:
                q.put(i)

        while not q.empty():
            t = q.get()
            res.append(t)
            for item in suffix[t]:
                idg = indgree[item] - 1
                indgree[item] = idg
                if idg == 0:
                    q.put(item)
        if len(res) != n:
            return []
        # print(res)
        return res


    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # O(n) 预处理未被分配的任务
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # 生成组间后缀关系
        groupPrefix = [set() for i in range(m)]
        groupSuffix = [set() for i in range(m)]
        for i in range(n):
            for item in beforeItems[i]:
                a = group[i]
                b = group[item]
                # b -> a
                if a != b:
                    groupPrefix[a].add(b)
                    groupSuffix[b].add(a)
        groupIndgree = [len(groupPrefix[i]) for i in range(m)]

        # 对组间进行拓扑排序
        groupNodes = [i for i in range(m)]
        groupTopSort = self.topSort(groupNodes, groupIndgree, groupSuffix)
        if len(groupTopSort) == 0:
            return groupTopSort

        # 预处理组内入度和后缀
        inGroupIndgree = [0 for i in range(n)]
        inGroupSuffix = [set() for i in range(n)]
        inGroupNodes = [[] for i in range(m)]
        for node in range(n):
            inGroupNodes[group[node]].append(node)
            for item in beforeItems[node]:
                # item -> node
                if group[node] == group[item]:
                    inGroupIndgree[node] += 1
                    inGroupSuffix[item].add(node)

        # 对每一组进行拓扑排序
        res = []
        for groupID in groupTopSort:
            inGroupTopSort = self.topSort(inGroupNodes[groupID], inGroupIndgree, inGroupSuffix)
            if len(inGroupTopSort) == 0 and len(inGroupNodes[groupID]) != 0:
                return []
            res += inGroupTopSort

        return res
'''


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        pass

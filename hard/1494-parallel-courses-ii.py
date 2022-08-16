'''
1494. 并行课程 II
给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， 
dependencies[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。

在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

 

示例 1：



输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
输出：3 
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
示例 2：



输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4 
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
示例 3：

输入：n = 11, dependencies = [], k = 2
输出：6
 

提示：

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
题目输入的图是个有向无环图。
'''

from collections import deque
from typing import List
'''
思路：拓扑排序
与普通的拓扑排序不同点在于，这个算法使用2个队列进行拓扑排序：
q1用于保存当前不需要先修的课程，q2用于保存当前课程修完后，变成可修的课程。
因为每个学期最多学k门课程，所以q1每消费完k个元素后，需要将学期+1
每当q1变空后，需要新启动一个新的学期才能开始q2的课程

时间复杂度：O(n^2)，时间复杂度取决于dependencies.length
空间复杂度：O(n^2)，构造邻接表需要的空间与dependencies.length相同

TODO  状态压缩
'''


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        q1, q2 = deque(), deque()
        count = 0  # 一个学期已经修完的课程
        ans = 0  # 学期
        indegree = [0] * (n + 1)  # 入度
        edges = [[] for _ in range(n + 1)]  # 邻接表
        for r in relations:
            indegree[r[1]] += 1  # 入度+1
            edges[r[0]].append(r[1])  # 将下一课程添加到邻接表
        for i in range(1, n + 1):  # 无先修的课程添加到q1中
            if indegree[i] == 0:
                q1.append(i)
        while q1:
            c = q1.popleft()
            count += 1
            if count > k:  # 如果已经修完的课程大于k，需要再添加一个学期
                count = 1
                ans += 1
                q1.extend(q2)
                q2 = deque()
            for nc in edges[c]:  # 遍历下一课程
                indegree[nc] -= 1
                if indegree[nc] == 0:
                    q2.append(nc)
            if not q1:  # 当前队列已无可修课程，修下一个队列，学期需要+1
                q1, q2 = q2, q1
                ans += 1
                count = 0
        return ans


s = Solution()
print(
    s.minNumberOfSemesters(13, [[12, 8], [2, 4], [3, 7], [6, 8], [11, 8], [9, 4], [9, 7], [12, 4], [11, 4], [6, 4], [1, 4], [10, 7], [10, 4], [1, 7], [1, 8],
                                [2, 7], [8, 4], [10, 8], [12, 7], [5, 4], [3, 4], [11, 7], [7, 4], [13, 4], [9, 8], [13, 8]], 9) == 3)  # TODO
print(s.minNumberOfSemesters(n=4, relations=[[2, 1], [3, 1], [1, 4]], k=2))
print(s.minNumberOfSemesters(n=5, relations=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))
print(s.minNumberOfSemesters(n=11, relations=[], k=2))

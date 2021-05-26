'''
面试题 04.01. 节点间通路
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。
'''
from typing import List
'''
思路：图的遍历
将图表示成邻接表的形式，然后从start出发DFS遍历图，如果能找到target则返回true，否则返回false

时间复杂度：O(n+e)
空间复杂度：O(n+e)
'''


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        g = [set() for _ in range(n)]
        for e in graph:
            if e[0] != e[1]:
                g[e[0]].add(e[1])
        visted = [False] * n

        def dfs(node):
            visted[node] = True
            for nextnode in g[node]:
                if not visted[nextnode]:
                    if nextnode == target:
                        return True
                    if dfs(nextnode):
                        return True
            return False

        return dfs(start)


s = Solution()
print(s.findWhetherExistsPath(n=3, graph=[[0, 1], [0, 2], [1, 2], [1, 2]], start=0, target=2))
print(s.findWhetherExistsPath(n=5, graph=[[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start=0, target=4))

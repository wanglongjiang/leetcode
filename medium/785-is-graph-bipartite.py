'''
判断二分图

存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，
其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，
都存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性:
不存在自环（graph[u] 不包含 u）。
不存在平行边（graph[u] 不包含重复值）。
如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，
就将这个图称为 二分图 。

如果图是二分图，返回 true ；否则，返回 false 。

 

示例 1：


输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
示例 2：


输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
 

提示：

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] 不会包含 u
graph[u] 的所有值 互不相同
如果 graph[u] 包含 v，那么 graph[v] 也会包含 u
'''
from typing import List
'''
思路：图的DFS遍历
根据题意，每个节点是否能唯一的设置为集合1或者集合2。需要遍历图中每个节点，尝试将其设置为集合之一。具体算法如下：
1. 遍历图的每个一个节点，将当前节点设置为1之后，与其直接相连的节点设置为2；反之如果将当前节点设置为2，则与其直接相连的节点设置为1
2. 上面的遍历过程中，如果某个节点之前被设置为集合a，在后面的遍历中又需要被设置为集合b，则这个图中的节点无法被二分。

与886.[可能的二分法](medium/886-possible-bipartition.py)相似

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0] * n

        # 遍历所有节点，为期分配一个集合编号
        def dfs(i, aggregate):
            visited[i] = aggregate
            nextAggregate = 1 if aggregate == 2 else 2
            for nexti in graph[i]:
                if visited[nexti]:  # 如果之前分配过集合，且之前的集合与本次想要分配的集合不一致，分配失败
                    if visited[nexti] != nextAggregate:
                        return False
                else:
                    if not dfs(nexti, nextAggregate):
                        return False
            return True

        for i in range(n):
            if not visited[i]:
                if not dfs(i, 1):
                    return False
        return True


s = Solution()
print(
    s.isBipartite([[2, 3, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 6, 9],
                   [0, 1, 2, 3, 7, 8, 9], [0, 1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9], [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]))
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))

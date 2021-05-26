'''
最小高度树

树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），
其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。

可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，
具有最小高度的树（即，min(h)）被称为 最小高度树 。

请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。

树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
 

示例 1：
输入：n = 4, edges = [[1,0],[1,2],[1,3]]
输出：[1]
解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。

示例 2：
输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
输出：[3,4]

示例 3：
输入：n = 1, edges = []
输出：[0]

示例 4：
输入：n = 2, edges = [[0,1]]
输出：[0,1]
 

提示：
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
所有 (ai, bi) 互不相同
给定的输入 保证 是一棵树，并且 不会有重复的边
'''
from typing import List
'''
思路：树的遍历
一个节点的最小高度为max(到所有子节点的高度，根节点到本节点的高度)
可以用深度优先遍历树，将上级节点的高度作为参数传给遍历函数，再遍历所有子节点的高度，得到该节点的最小高度
然后将最大的子节点高度返回给上级函数
算法如下：
> 1. 遍历edges建立邻接表形式的树
> 2. 深度优先遍历树，求出每个子节点的最小高度，如果某个子节点高于所有子节点和根节点高度，需要将该高度再修正其他较小的子节点
> 3. 遍历所有节点的最小高度，找出最小的那些输出

时间复杂度：O(n)
空间复杂度：O(n)
TODO
'''


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. 建立邻接表
        tree = [[] for _ in range(n)]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        # 2. 深度优先遍历树，求出每个节点的最小高度
        minHeights = [0] * n

        visted = [False] * n

        def dfs(i, rootHeight):
            visted[i] = True
            rootHeight += 1
            height = 0
            for j in tree[i]:
                if not visted[j]:
                    height = max(height, dfs(j, rootHeight))
            minHeights[i] = max(height, rootHeight)
            return height

        dfs(0, 0)

        visted = [False] * n

        def fixHeight(i, rootHeight):
            visted[i] = True
            rootHeight += 1
            height = 0
            for j in tree[i]:
                if not visted[j]:
                    height = max(height, dfs(j, minHeights[i]))
            minHeights[i] = max(height, rootHeight)
            return height

        fixHeight(0, 0)
        # 3. 遍历所有节点的最小高度，找出最小的那些输出
        minHeight = min(minHeights)
        return list(filter(lambda x: x == minHeight, minHeights))


s = Solution()
print(s.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
print(s.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
print(s.findMinHeightTrees(n=1, edges=[]))
print(s.findMinHeightTrees(n=2, edges=[[0, 1]]))

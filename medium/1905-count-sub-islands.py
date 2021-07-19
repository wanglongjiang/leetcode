'''
统计子岛屿
给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。
一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。

如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，
那么我们称 grid2 中的这个岛屿为 子岛屿 。

请你返回 grid2 中 子岛屿 的 数目 。

 

示例 1：


输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
输出：3
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
示例 2：


输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
 grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
输出：2
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
 

提示：

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-sub-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import deque
'''
思路：BFS+并查集
1. 用BFS遍历grid2所有的单元格，然后将岛屿加入并查集union1,union2
2. 再次遍历grid1、grid2，
> 如果grid2[i][j]为1，grid1[i][j]为1，将其grid2的根节点加入哈希集合issub
> 如果grid2[i][j]为1，grid1[i][j]为0，说明岛屿已经超出grid1的范围，将根节点加入哈希集合notsub
3. issub-notsub即为所有的子岛屿根节点

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


# 定义并查集
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        # BFS遍历矩阵，加入并查集
        def bfs(grid):
            unionFind = UnionFind(m * n)
            marked = [[False] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not marked[i][j]:
                        q = deque()
                        q.append((i, j))
                        marked[i][j] = True
                        while q:
                            x, y = q.popleft()
                            for nextx, nexty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                                if 0 <= nextx < m and 0 <= nexty < n and grid[nextx][nexty] and not marked[nextx][nexty]:
                                    q.append((nextx, nexty))
                                    marked[nextx][nexty] = True
                                    unionFind.union(x * n + y, nextx * n + nexty)
            return unionFind

        union2 = bfs(grid2)
        # 再次遍历grid1、grid2，判断grid2的单元格是否是子岛屿
        issub, notsub = set(), set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    if grid1[i][j]:
                        issub.add(union2.find(i * n + j))
                    else:
                        notsub.add(union2.find(i * n + j))
        return len(issub - notsub)


s = Solution()
print(
    s.countSubIslands(grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                      grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
print(
    s.countSubIslands(grid1=[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                      grid2=[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))

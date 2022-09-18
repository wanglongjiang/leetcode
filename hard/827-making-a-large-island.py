'''
827. 最大人工岛
给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。

返回执行此操作后，grid 中最大的岛屿面积是多少？

岛屿 由一组上、下、左、右四个方向相连的 1 形成。

 

示例 1:

输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:

输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:

输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
 

提示：

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] 为 0 或 1
'''
from collections import defaultdict
from typing import List
'''
思路：并查集
首先，遍历所有的陆地单元格，检查其4个相邻单元格是否为陆地，如果是陆地，可以连结起来，将这个连结用并查集保存起来。
然后，遍历每个陆地单元格，检查其所属的岛屿，计算岛屿面积，把岛屿的面积用哈希表记录下来（key为并查集的根节点，value为岛屿面积）。
最后，遍历所有的海洋单元格，与该单元格连结的岛屿会形成一个面积更大的岛屿，在该遍历过程中寻找能形成的最大岛屿。
    
时间复杂度：O(n^2)，3次遍历矩阵的时间复杂度都是O(n^2)
空间复杂度：O(n^2)，并查集需要的空间是O(n^2)，保存岛屿面积需要的空间复杂度是O(n^2)
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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 首先遍历陆地，将相邻陆地保存到并查集，形成岛屿
        uf = UnionFind(n * n)
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    continue
                no = i * n + j
                for nexti, nextj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= nexti < n and 0 <= nextj < n and grid[nexti][nextj]:
                        uf.union(no, nexti * n + nextj)
        # 遍历所有的陆地，计算每个岛屿面积
        islandArea = defaultdict(int)
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    islandArea[uf.find(i * n + j)] += 1
                    ans = max(ans, islandArea[uf.find(i * n + j)])
        # 遍历所有的海洋，计算与其相邻的岛屿面积形成新岛屿后的面积，找到面积最大的
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                islands = set()  # 将相邻的岛屿加入哈希表去重
                for nexti, nextj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= nexti < n and 0 <= nextj < n and grid[nexti][nextj]:
                        islands.add(uf.find(nexti * n + nextj))
                ans = max(ans, sum(islandArea[island] for island in islands) + 1)  # 形成的新岛屿面积是周边岛屿之和+1
        return ans


s = Solution()
print(s.largestIsland([[1, 1], [1, 1]]))
print(s.largestIsland([[1, 1], [1, 0]]))

'''
2328. 网格图中递增路径的数目
给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。

请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。
由于答案可能会很大，请将结果对 109 + 7 取余 后返回。

如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。

 

示例 1：



输入：grid = [[1,1],[3,4]]
输出：8
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[1]，[3]，[4] 。
- 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
- 长度为 3 的路径：[1 -> 3 -> 4] 。
路径数目为 4 + 3 + 1 = 8 。
示例 2：

输入：grid = [[1],[2]]
输出：3
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[2] 。
- 长度为 2 的路径：[1 -> 2] 。
路径数目为 2 + 1 = 3 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105
'''
from typing import List
'''
思路：动态规划 排序
将单元格按照值排序，然后从小到大遍历所有单元格。
对于单元格grid[i][j]，经过以其为终点的路径为1+sum(四周比grid[i][j]小的单元格路径数)

时间复杂度：O(mnlog(mn))
空间复杂度：O(mn)
'''


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, modu = len(grid), len(grid[0]), 10**9 + 7
        ans = [[1] * n for _ in range(m)]
        grids = []
        for i in range(m):
            for j in range(n):
                grids.append((grid[i][j], i, j))
        grids.sort()
        for val, i, j in grids:
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if m > x >= 0 and n > y >= 0 and val > grid[x][y]:
                    ans[i][j] += ans[x][y] % modu
        return sum(sum(row) % modu for row in ans) % modu


s = Solution()
print(s.countPaths([[1, 1], [3, 4]]))
print(s.countPaths([[1], [2]]))

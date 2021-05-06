'''
矩阵中的最长递增路径

给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

 

示例 1：
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。

示例 2：
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

示例 3：
输入：matrix = [[1]]
输出：1
 

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
'''
from typing import List
'''
思路：暴力搜索+记忆化
从每个单元格出发，遍历所有路径（能前进的路径为递增序列），将最长的路径返回
遍历过程中，设置一个m*n的路径长度，记忆每个单元格出发的路径长度
时间复杂度：O(m*n*k)，k为平均路径长度
空间复杂度：O(m*n)
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        lens = [[0] * n for _ in range(m)]  # 记忆数组
        directs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # 搜索从某一单元格出发的路径长度
        def dfs(i, j):
            if lens[i][j]:
                return lens[i][j]
            maxlen = 1
            for a, b in directs:
                x, y = a + i, b + j
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    maxlen = max(maxlen, 1 + dfs(x, y))
            lens[i][j] = maxlen
            return maxlen

        ans = 0
        # 遍历每个单元格开始的路径长度
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


s = Solution()
print(s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
print(s.longestIncreasingPath([[1]]))

'''
矩阵区域和
给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - k <= r <= i + k,
j - k <= c <= j + k 且
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：前缀和
题目就是求以i,j为中心的边长为2k+1的矩阵元素和
可以先求整个矩阵的前缀和
然后用矩阵右下角的前缀和-子矩阵上部前缀和-子矩阵右边前缀和+子矩阵左上矩阵前缀和

时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        sums = [[0] * n for _ in range(m)]
        # 求前缀和
        for i in range(m):
            for j in range(n):
                sums[i][j] = mat[i][j] + (sums[i - 1][j] if i > 0 else 0) + (sums[i][j - 1] if j > 0 else 0) - (sums[i - 1][j - 1] if i > 0 and j > 0 else 0)
        # 求结果
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                right, bottom = min(j + k, n - 1), min(i + k, m - 1)
                left, top = j - k - 1, i - k - 1
                ans[i][j] = sums[bottom][right] - (sums[top][right] if top >= 0 else 0) - (sums[bottom][left] if left >= 0 else
                                                                                           0) + (sums[top][left] if top >= 0 and left >= 0 else 0)
        return ans

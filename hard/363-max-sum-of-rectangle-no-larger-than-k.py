'''
矩形区域不超过 K 的最大数值和

给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。
提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5
'''
from typing import List
'''
思路：前缀和
1、求出每个坐标的前缀和,对于i,j来说也就是矩阵0,0至i,j的矩阵和
2、遍历每个坐标，求其与右、下每个坐标形成的矩阵的和，这个过程中计算与k的差。
优化：因为矩阵中每个元素值-100 <= matrix[i][j] <= 100，-10^5 <= k <= 10^5，
可以得到最少需要的元素数minItems=k/100
第2步遍历矩阵时，需要确保矩阵里面的元素数>=minItems

时间复杂度：O(m*n*m*n)
空间复杂度：O(m*n)

PS.python未通过，java通过了
'''


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        minItems = k // 100 + (0 if k % 100 == 0 else 1)  # 最少需要的元素数
        # 1、求矩阵的前缀和
        sums = [[0] * (n + 1) for _ in range(m + 1)]  # 前缀和矩阵有多余的1行、1列，简化边界条件判断
        for i in range(m):
            for j in range(n):
                sums[i + 1][j + 1] = matrix[i][j] + sums[i][j + 1] + sums[i + 1][j] - sums[i][j]
        diff = float('inf')
        # 2、遍历每个坐标，求其与右、下每个坐标形成的矩阵的和与k的差
        for i in range(1, m + 1):
            if (m + 1 - i) * (n) < minItems:  # 矩阵最大大小已不满足最少元素数，退出循环
                break
            for j in range(1, n + 1):
                if (m + 1 - i) * (n + 1 - j) < minItems:  # 矩阵最大大小已不满足最少元素数，退出循环
                    break
                for bottom in range(m, i - 1, -1):  # 从下到上缩小范围
                    if (bottom + 1 - i) * (n + 1 - j) < minItems:  # 矩阵最大大小已不满足最少元素数，退出循环
                        break
                    for right in range(n, j - 1, -1):  # 从右至左缩小范围
                        if (bottom + 1 - i) * (right + 1 - j) < minItems:  # 矩阵最大大小已不满足最少元素数，退出循环
                            break
                        # 求2个坐标形成的矩阵和
                        s = sums[i - 1][j - 1] + sums[bottom][right] - sums[i - 1][right] - sums[bottom][j - 1]
                        if s <= k and k - s < diff:
                            diff = k - s
                            if diff == 0:
                                return k
        return k - diff


s = Solution()
print(s.maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))
print(s.maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))

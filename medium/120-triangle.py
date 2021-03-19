'''
三角形最小路径和
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
from typing import List
'''
思路：动态规划。
对于三角形第i行，第j个元素来说，有动态规划状态转移方程：
1、最短路径p[i][j] = min(p[i-1][j],p[i-1][j-1])，
2、p[0][0] = 0
最后求最后一行的最小值，即为最小路径
时间复杂度：O(n*n)，每个元素遍历一次
空间复杂度：O(n*n)，

'''


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        path = [None] * n
        path[0] = triangle[0]
        for i in range(1, n):
            path[i] = [float('inf')] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    path[i][j] = path[i - 1][j] + triangle[i][j]
                elif i == j:
                    path[i][j] = path[i - 1][j - 1] + triangle[i][j]
                else:
                    path[i][j] = min(path[i - 1][j - 1] + triangle[i][j], path[i - 1][j] + triangle[i][j])
        return min(path[n - 1])


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(s.minimumTotal([[-10]]))

'''
1351. 统计有序矩阵中的负数
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 grid 中 负数 的数目。

 

示例 1：

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
示例 2：

输入：grid = [[3,2],[1,0]]
输出：0
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

进阶：你可以设计一个时间复杂度为 O(n + m) 的解决方案吗？
'''

from typing import List
'''
思路：贪心
先搜索第1行的第1个负数，设坐标为0,j，那么下一行的第1个负数坐标1,有k<=j。因为根据题意按照列也是非递增的。
这样每一行的第1个负数列都<=上一行的列。
算法主要思路：
1、搜索第1行，找到第1个负数，其列为maxCol
2、迭代所有的行，对于每行，从maxCol向前搜索，遇到第1个非负数停止，同时更新maxCol

时间复杂度：O(n+m)，行坐标只迭代一次，列坐标也只会迭代一次
空间复杂度：O(n+m)
'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for col in range(n - 1, -1, -1):  # 先找到第1行的第1个负数
            if grid[0][col] >= 0:
                ans += n - col - 1
                break
        else:  # 第一行全部是负数
            ans += n
        maxCol = min(n - ans - 1, n - 1)  # 负数最大列坐标
        for row in range(1, m):
            for col in range(maxCol, -1, -1):
                if grid[row][col] >= 0:
                    ans += n - col - 1
                    maxCol = col
                    break
            else:  # 一行全部都是0，后面的行不需要再统计
                ans += n * (m - row)
                break
        return ans


s = Solution()
print(s.countNegatives([[3, 2], [-3, -3], [-3, -3], [-3, -3]]))
print(s.countNegatives([[-1]]))
print(s.countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(s.countNegatives([[3, 2], [1, 0]]))

'''
2482. 行和列中一和零的差值
中等
1
相关企业
给你一个下标从 0 开始的 m x n 二进制矩阵 grid 。

我们按照如下过程，定义一个下标从 0 开始的 m x n 差值矩阵 diff ：

令第 i 行一的数目为 onesRowi 。
令第 j 列一的数目为 onesColj 。
令第 i 行零的数目为 zerosRowi 。
令第 j 列零的数目为 zerosColj 。
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
请你返回差值矩阵 diff 。

 

示例 1：



输入：grid = [[0,1,1],[1,0,1],[0,0,1]]
输出：[[0,0,4],[0,0,4],[-2,-2,2]]
解释：
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2
示例 2：



输入：grid = [[1,1,1],[1,1,1]]
输出：[[5,5,5],[5,5,5]]
解释：
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] 要么是 0 ，要么是 1 。
'''
from typing import List
'''
[TOC]

# 思路
模拟

# 解题方法
先统计每行、每列1的个数，然后模拟题意，计算每个单元格的答案

# 复杂度
- 时间复杂度: 
> $O(mn)$ 

- 空间复杂度: 
> $O(mn)$
'''


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rowCount, colCount = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rowCount[i] += 1
                    colCount[j] += 1
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rowCount[i] + colCount[j] - m + rowCount[i] - n + colCount[j]
        return diff


s = Solution()
assert s.onesMinusZeros([[1, 1, 1], [1, 1, 1]]) == [[5, 5, 5], [5, 5, 5]]
assert s.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]) == [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]

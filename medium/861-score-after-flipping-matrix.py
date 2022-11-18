'''
861. 翻转矩阵后的得分
中等
232
相关企业
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1
'''
from typing import List
'''
[TOC]

# 思路
贪心

# 解题方法
1. 先使用行变换，将第1列的0全变成1
2. 遍历每一列，如果0的数量>=1的数量，使用列变换
3. 合并结果

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 1. 先使用行变换，将第1列的0全变成1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        # 2. 遍历每一列，如果0的数量>=1的数量，使用列变换
        for j in range(n):
            oneCnt = 0
            for i in range(m):
                oneCnt += grid[i][j]
            if oneCnt < m / 2:
                for i in range(m):
                    grid[i][j] ^= 1
        # 3. 合并结果
        ans = 0
        for i in range(m):
            r = 0
            for j in range(n):
                r = (r << 1) | grid[i][j]
            ans += r
        return ans


s = Solution()
assert s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39

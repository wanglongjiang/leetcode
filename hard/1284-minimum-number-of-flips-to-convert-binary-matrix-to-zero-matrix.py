'''
1284. 转化为全零矩阵的最少反转次数
困难
62
相关企业
给你一个 m x n 的二进制矩阵 mat。每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。
如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。

请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。

二进制矩阵 的每一个格子要么是 0 要么是 1 。

全零矩阵 是所有格子都为 0 的矩阵。

 

示例 1：



输入：mat = [[0,0],[0,1]]
输出：3
解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
示例 2：

输入：mat = [[0]]
输出：0
解释：给出的矩阵是全零矩阵，所以你不需要改变它。
示例 3：

输入：mat = [[1,0,0],[1,0,0]]
输出：-1
解释：该矩阵无法转变成全零矩阵
 

提示：

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] 是 0 或 1 。
'''
from collections import deque
from typing import List
'''
[TOC]

# 思路
BFS 位运算

# 解题方法
> 输入的矩阵很小，最大是3*3，那么可以用一个整数的位映射矩阵的每个单元格，用BFS遍历所有的状态，如果有状态为全0，则返回反转次数

# 复杂度
- 时间复杂度: 
>  $O(2^(m*n))$，最多有9个单元格，所以最大为2^9

- 空间复杂度: 
> $O(2^(m*n))$
'''


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        status = 0
        # 状态压缩
        for i in range(m):
            for j in range(n):
                status = (status << 1) | mat[i][j]
        ans, queue, marked = 0, deque(), set()
        queue.append(status)
        marked.add(status)
        while queue:
            size = len(queue)
            for _ in range(size):
                status = queue.popleft()
                if status == 0:
                    return ans
                # 遍历所有的单元格，将其进行反转
                for i in range(m):
                    for j in range(n):
                        nextStatus = status ^ (1 << (i * n + j))  # 将i,j取反
                        # 将i,j周围的单元格取反
                        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= r < m and 0 <= c < n:
                                nextStatus ^= 1 << (r * n + c)  # 将r,c取反
                        if nextStatus not in marked:  # 该状态之前未处理过，加入队列待处理
                            marked.add(nextStatus)
                            queue.append(nextStatus)
            ans += 1
        return -1


s = Solution()
assert s.minFlips([[0, 0], [0, 1]]) == 3
assert s.minFlips([[0]]) == 0
assert s.minFlips([[1, 0, 0], [1, 0, 0]]) == -1

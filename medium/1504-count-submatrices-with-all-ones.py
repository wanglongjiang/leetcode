'''
1504. 统计全 1 子矩形
给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

示例 1：



输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：



输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。

 

提示：

1 <= m, n <= 150
mat[i][j] 仅包含 0 或 1
'''
from typing import List
'''
单调栈
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        row = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1

        ans = 0
        for j in range(m):
            Q = list()
            total = 0
            for i in range(n):
                height = 1
                while Q and Q[-1][0] > row[i][j]:
                    # 弹出的时候要减去多于的答案
                    total -= Q[-1][1] * (Q[-1][0] - row[i][j])
                    height += Q[-1][1]
                    Q.pop()
                total += row[i][j]
                ans += total
                Q.append((row[i][j], height))

        return ans

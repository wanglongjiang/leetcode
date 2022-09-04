'''
1582. 二进制矩阵中的特殊位置
给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。

特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），
则位置 (i, j) 被称为特殊位置。

 

示例 1：

输入：mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]
输出：1
解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0
示例 2：

输入：mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
输出：3
解释：(0,0), (1,1) 和 (2,2) 都是特殊位置
示例 3：

输入：mat = [[0,0,0,1],
            [1,0,0,0],
            [0,1,1,0],
            [0,0,0,0]]
输出：2
示例 4：

输入：mat = [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
输出：3
 

提示：

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] 是 0 或 1
'''
from typing import List
'''
思路：模拟
设2个哈希表usedCols和ngCols，分别保存已经使用过的列和已经淘汰的列，二个集合大小的差即为特殊位置

时间复杂度：O(mn)
空间复杂度：O(n)
'''


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        usedCols, ngCols = set(), set()
        for row in mat:
            count = 0
            for col, val in enumerate(row):
                if val:
                    count += 1
                    if col in usedCols:  # 该列之前使用过，该列的坐标都需要取消特殊位置的资格
                        ngCols.add(col)
                    else:  # 该列之前未使用过，加入已使用过的列集合
                        usedCols.add(col)
            if count > 1:  # 该行多于1个1，所有的列都需要取消特殊位置的资格
                for col, val in enumerate(row):
                    if val:
                        ngCols.add(col)
        return len(usedCols) - len(ngCols)

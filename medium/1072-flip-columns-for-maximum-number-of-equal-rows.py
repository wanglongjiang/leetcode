'''
1072. 按列翻转得到最大值等行数
给定 m x n 矩阵 matrix 。

你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）

返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。

 

示例 1：

输入：matrix = [[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。
示例 2：

输入：matrix = [[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。
示例 3：

输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] == 0 或 1
'''
from typing import Counter, List
'''
思路：哈希
对于2行记录row1,row2，如果每个元素全都相同，也就是row1[i]==row2[i]，或者全都不相同，row1[i]!=row2[i]。
那么这2行可以通过翻转相同的列变成一行相同。
可以将每行转成元组加入哈希表，然后每行的翻转也加入哈希表计数，具有相同key的可以通过翻转相同的列变成整行相同。

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        for row in matrix:
            count[tuple(row)] += 1
            count[tuple(i ^ 1 for i in row)] += 1
        return count.most_common(1)[0][1]


s = Solution()
print(s.maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
print(s.maxEqualRowsAfterFlips([[0, 1], [1, 1]]))

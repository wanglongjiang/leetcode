'''
959. 由斜杠划分区域
在由 1 x 1 方格组成的 n x n 网格 grid 中，每个 1 x 1 方块由 '/'、'\' 或空格构成。这些字符会将方块划分为一些共边的区域。

给定网格 grid 表示为一个字符串数组，返回 区域的数量 。

请注意，反斜杠字符是转义的，因此 '\' 用 '\\' 表示。

 

示例 1：



输入：grid = [" /","/ "]
输出：2
示例 2：



输入：grid = [" /","  "]
输出：1
示例 3：



输入：grid = ["/\\","\\/"]
输出：5
解释：回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。
 

提示：

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] 是 '/'、'\'、或 ' '
'''

from typing import List
'''
思路：并查集
每个单元格有可能被切分成左上、右下或者右上、左下，然后我们可以把一个单元格视为由4部分构成：上、下、左、右。
当单元格被'/'切分时，上、左是联通的，下、右是联通的，
当单元格被'\\'切分时，上、右是联通的，下、左是联通的，
当单元格为空格时，4部分都是联通的，
此外，上、下、左、右分别与4个相邻单元格联通。

遍历矩阵，将每个单元格内的4部分的联通关系加入并查集，最后查询并查集即可。

时间复杂度：O(n^2)
空间复杂度：O(N^2)
'''


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n * n * 4)  # 共n*n*4个小单元格。上下左右的小编号分别是0、1、2、3
        for i, s in enumerate(grid):
            for j, char in enumerate(s):
                baseNo = i * n + j
                if char == '/':
                    uf.union((baseNo << 2), (baseNo << 2) + 2)  # 上左联通
                    uf.union((baseNo << 2) + 1, (baseNo << 2) + 3)  # 下右联通
                elif char == '\\':
                    uf.union((baseNo << 2), (baseNo << 2) + 3)  # 上右联通
                    uf.union((baseNo << 2) + 1, (baseNo << 2) + 2)  # 下左联通
                else:  # 4个格均联通
                    uf.union((baseNo << 2), (baseNo << 2) + 1)
                    uf.union((baseNo << 2), (baseNo << 2) + 2)
                    uf.union((baseNo << 2), (baseNo << 2) + 3)
                if i > 0:  # 与上面的单元格的下部联通
                    uf.union((baseNo << 2), ((baseNo - n) << 2) + 1)
                if j > 0:  # 与左边单元格的右部联通
                    uf.union((baseNo << 2) + 2, ((baseNo - 1) << 2) + 3)
                if i < n - 1:  # 与下面单元格的上部联通
                    uf.union((baseNo << 2) + 1, (baseNo + n) << 2)
                if j < n - 1:  # 与右边单元格的左部联通
                    uf.union((baseNo << 2) + 3, ((baseNo + 1) << 2) + 2)
        return len(set(uf.find(i) for i in range(n * n * 4)))


s = Solution()
print(s.regionsBySlashes([" /", "/ "]))
print(s.regionsBySlashes([" /", "  "]))
print(s.regionsBySlashes(["/\\", "\\/"]))

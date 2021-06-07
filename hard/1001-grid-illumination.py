'''
网格照明
在 N x N 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

数组 lamps 表示打开的灯的位置。lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的第 i 盏灯 。
每盏灯都照亮自身单元格以及同一行、同一列和两条对角线上的所有其他单元格。

查询数组 queries 中，第 i 次查询 queries[i] = [rowi, coli]，如果单元格 [rowi, coli] 是被照亮的，则查询结果为 1 ，否则为 0 。
在第 i 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowi][coli] 上或其相邻 8 个方向上
（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

返回答案数组 ans ， answer[i] 应等于第 i 次查询 queries[i] 的结果，1 表示照亮，0 表示未照亮。

 

示例 1：


输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。
该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。

第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。

示例 2：

输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]
示例 3：

输入：N = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]
 

提示：

1 <= N <= 10^9
0 <= lamps.length <= 20000
lamps[i].length == 2
0 <= lamps[i][j] < N
0 <= queries.length <= 20000
queries[i].length == 2
0 <= queries[i][j] < N
'''
from typing import List
from collections import defaultdict
'''
思路：哈希
如何判定是否被照亮：
> 同行，同列容易判定，建立以行、列索引为key的哈希表即可
> 左上右下的对角线，x-y是个固定值，可以建立以这个差作为key的哈希表
> 右上左下的对角线，x+y是个固定值，可以建立以这个和作为key的哈希表

如何灭灯：
建立以x,y为key的哈希表，针对每个查询，查看其四周的9个坐标是否有值，
如果有，将其从5个哈希表中删除。

时间复杂度：O(m+k),m为lamps.length,k为queries.length
空间复杂度：O(m)
'''


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        m, k = len(lamps), len(queries)
        # 建立5个哈希表，key分别为坐标索引、行索引、列索引、左对角线、右对角线,value为在矩阵中的坐标
        idxHash, rowHash, colHash, leftTopHash, rightTopHash = {}, defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(m):
            row, col = lamps[i][0], lamps[i][1]
            idx = row * n + col
            idxHash[idx] = i
            rowHash[row].add(idx)
            colHash[col].add(idx)
            leftTopHash[row - col].add(idx)
            rightTopHash[row + col].add(idx)
        # 遍历所有查询，进行查询和灭灯
        ans = [0] * k
        for i in range(k):
            row, col = queries[i][0], queries[i][1]
            if (row * n + col) in idxHash or rowHash[row] or colHash[col] or leftTopHash[row - col] or rightTopHash[row + col]:
                ans[i] = 1
            # 遍历9个位置，进行灭灯
            for xOff, yOff in [(0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                x, y = xOff + row, yOff + col
                if 0 <= x < n and 0 <= y < n:
                    idx = x * n + y
                    if idx in idxHash:
                        del idxHash[idx]
                        rowHash[x].remove(idx)
                        colHash[y].remove(idx)
                        leftTopHash[x - y].remove(idx)
                        rightTopHash[x + y].remove(idx)
        return ans


s = Solution()
print(
    s.gridIllumination(6, [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]], [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]) ==
    [1, 0, 1, 1, 0, 1])
print(s.gridIllumination(n=5, lamps=[[0, 0], [0, 4]], queries=[[0, 4], [0, 1], [1, 4]]) == [1, 1, 0])
print(s.gridIllumination(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 0]]) == [1, 0])
print(s.gridIllumination(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 1]]) == [1, 1])

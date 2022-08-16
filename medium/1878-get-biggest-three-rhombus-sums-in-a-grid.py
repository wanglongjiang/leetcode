'''
1878. 矩阵中最大的三个菱形和
给你一个 m x n 的整数矩阵 grid 。

菱形和 指的是 grid 中一个正菱形 边界 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。
下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。


 

注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。

请你按照 降序 返回 grid 中三个最大的 互不相同的菱形和 。如果不同的和少于三个，则将它们全部返回。

 

示例 1：


输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
输出：[228,216,211]
解释：最大的三个菱形和如上图所示。
- 蓝色：20 + 3 + 200 + 5 = 228
- 红色：200 + 2 + 10 + 4 = 216
- 绿色：5 + 200 + 4 + 2 = 211
示例 2：


输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：[20,9,8]
解释：最大的三个菱形和如上图所示。
- 蓝色：4 + 2 + 6 + 8 = 20
- 红色：9 （右下角红色的面积为 0 的菱形）
- 绿色：8 （下方中央面积为 0 的菱形）
示例 3：

输入：grid = [[7,7,7]]
输出：[7]
解释：所有三个可能的菱形和都相同，所以返回 [7] 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 105
'''
from heapq import heappushpop, heapreplace
from typing import List
'''
思路：矩阵 堆（优先队列）
遍历矩阵的每个单元格，遍历以其为底角的所有菱形和，然后将其加入大小为3的堆中。
为快速计算菱形和，需要设置2个辅助矩阵，分别保存向左上和向右上的前缀和。TODO


时间复杂度：O(mnn)
空间复杂度：O(1)
'''


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        heap = [0, 0, 0]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != heap[0] and grid[i][j] != heap[1] and grid[i][j] != heap[2] and grid[i][j] > heap[0]:
                    heapreplace(heap, grid[i][j])
                w = 1
                while (j - w) >= 0 and (j + w) < n and (i - 2 * w) >= 0:  # 判断菱形的4个坐标均合法
                    s = grid[i][j] + grid[i - w][j - w] + grid[i - w][j + w] + grid[i - 2 * w][j]
                    if s != heap[0] and s != heap[1] and s != heap[2] and s > heap[0]:
                        heapreplace(heap, s)
                    w += 1
        ans = [x for x in heap if x > 0]
        ans.sort(reverse=True)
        return ans


s = Solution()
print(
    s.getBiggestThree([[20, 17, 9, 13, 5, 2, 9, 1, 5], [14, 9, 9, 9, 16, 18, 3, 4, 12], [18, 15, 10, 20, 19, 20, 15, 12, 11],
                       [19, 16, 19, 18, 8, 13, 15, 14, 11], [4, 19, 5, 2, 19, 17, 7, 2, 2]]) == [107, 103, 102])

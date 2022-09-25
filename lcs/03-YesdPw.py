'''
LCS 03. 主题空间
「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 grid，
字符串中仅包含 "0"～"5" 这 6 个字符。地图上每一个字符代表面积为 1 的区域，其中 "0" 表示走廊，其他字符表示主题空间。
相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。

假如整个 grid 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 0。

示例 1:

输入：grid = ["110","231","221"]

输出：1

解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。
image.png

示例 2:

输入：grid = ["11111100000","21243101111","21224101221","11111101111"]

输出：3

解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。
image.png

提示：

1 <= grid.length <= 500
1 <= grid[i].length <= 500
grid[i][j] 仅可能是 "0"～"5"
'''
from typing import List
'''
思路：DFS
用DFS遍历所有的主题空间，遍历过程中如果发现某个单元格与处于边界或者与0相邻，则该空间不统计面积

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        marked = [[False] * n for _ in range(m)]

        def dfs(x, y):
            marked[x][y] = True
            area = 1
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                area = 0
            if x > 0 and not marked[x - 1][y]:
                if grid[x - 1][y] == '0':
                    area = 0
                elif grid[x - 1][y] == grid[i][j]:
                    oarea = dfs(x - 1, y)
                    area = oarea + area if oarea and area else 0
            if y > 0 and not marked[x][y - 1]:
                if grid[x][y - 1] == '0':
                    area = 0
                elif grid[x][y - 1] == grid[i][j]:
                    oarea = dfs(x, y - 1)
                    area = oarea + area if oarea and area else 0
            if x < m - 1 and not marked[x + 1][y]:
                if grid[x + 1][y] == '0':
                    area = 0
                elif grid[x + 1][y] == grid[i][j]:
                    oarea = dfs(x + 1, y)
                    area = oarea + area if oarea and area else 0
            if y < n - 1 and not marked[x][y + 1]:
                if grid[x][y + 1] == '0':
                    area = 0
                elif grid[x][y + 1] == grid[i][j]:
                    oarea = dfs(x, y + 1)
                    area = oarea + area if oarea and area else 0
            return area

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '0' and not marked[i][j]:
                    ans = max(dfs(i, j), ans)
        return ans


s = Solution()
print(s.largestArea(grid=["110", "231", "221"]))
print(s.largestArea(["11111100000", "21243101111", "21224101221", "11111101111"]))

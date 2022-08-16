'''
361. 轰炸敌人
想象一下炸弹人游戏，在你面前有一个二维的网格来表示地图，网格中的格子分别被以下三种符号占据：

'W' 表示一堵墙
'E' 表示一个敌人
'0'（数字 0）表示一个空位


请你计算一个炸弹最多能炸多少敌人。

由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。

注意：你只能把炸弹放在一个空的格子里

示例:

输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
输出: 3
解释: 对于如下网格

0 E 0 0
E 0 W E
0 E 0 0

假如在位置 (1,1) 放置炸弹的话，可以炸到 3 个敌人
'''
from typing import List
'''
思路：矩阵
设置2个辅助矩阵，rowGrid,colGrid。
rowGrid用于保存某个空位在这一行，最多能炸到的敌人，
colGrid用于保存某个空位在这一列，最多能炸到的敌人，
某个空位能炸到的最多的敌人就是rowGrid和colGrid之和。
rowGrid和colGrid就比较容易计算了，2堵墙之间的空位能炸到的敌人数是相同的，就是2堵墙内的敌人数量。
嗯，rowGrid和colGrid也可以合并，先计算行上的，然后计算列上的。


时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        tgrid = [[0] * n for _ in range(m)]  # 辅助计算用的矩阵
        # 先计算在一行里面，一个空位能炸到的最多的敌人
        for i in range(m):
            left, right = 0, 0
            while right < n:
                ecount, scount = 0, 0  # 记录2堵墙之间的敌人、空位数量
                while right < n and grid[i][right] != 'W':
                    if grid[i][right] == 'E':
                        ecount += 1
                    else:
                        scount += 1
                    right += 1
                for k in range(left, right):
                    if grid[i][k] == '0':
                        tgrid[i][k] = ecount  # 将空位能炸到的敌人数进行更新
                left = right
                while right < n and grid[i][right] == 'W':  # 越过墙
                    right += 1
        # 再计算一列里面，一个空位能炸到的最多的敌人
        ans = 0
        for j in range(m):
            top, bottom = 0, 0
            while bottom < m:
                ecount, scount = 0, 0  # 记录2堵墙之间的敌人、空位数量
                while bottom < m and grid[bottom][j] != 'W':
                    if grid[bottom][j] == 'E':
                        ecount += 1
                    else:
                        scount += 1
                    bottom += 1
                for k in range(top, bottom):
                    if grid[k][j] == '0':
                        tgrid[k][j] += ecount  # 将空位能炸到的敌人数进行更新
                        ans = max(ans, tgrid[k][j])
                top = bottom
                while bottom < m and grid[bottom][j] == 'W':  # 越过墙
                    bottom += 1
        return ans


s = Solution()
print(s.maxKilledEnemies([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]))

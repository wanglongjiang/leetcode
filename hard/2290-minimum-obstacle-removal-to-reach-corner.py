'''
2290. 到达角落需要移除障碍物的最小数目
给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n 。每个单元格都是两个值之一：

0 表示一个 空 单元格，
1 表示一个可以移除的 障碍物 。
你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。

现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1) ，返回需要移除的障碍物的 最小 数目。

 

示例 1：



输入：grid = [[0,1,1],[1,1,0],[1,1,0]]
输出：2
解释：可以移除位于 (0, 1) 和 (0, 2) 的障碍物来创建从 (0, 0) 到 (2, 2) 的路径。
可以证明我们至少需要移除两个障碍物，所以返回 2 。
注意，可能存在其他方式来移除 2 个障碍物，创建出可行的路径。
示例 2：



输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
输出：0
解释：不移除任何障碍物就能从 (0, 0) 到 (2, 4) ，所以返回 0 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] 为 0 或 1
grid[0][0] == grid[m - 1][n - 1] == 0
'''
from collections import deque
from typing import List
'''
思路：BFS
与通常的BFS不同点在于：
设2个队列，从0到0和从1到0的路径成本为0，加入当前队列；从0到1和从1到1的路径，成本为1，加入备用队列。
当当前队列为空时，切换为备用队列，同时需要移除的障碍+1。

时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q1, q2 = deque(), deque()
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        marked = [[False] * n for _ in range(m)]
        ans = 0
        q1.append((0, 0))
        marked[0][0] = True
        while q1:
            x, y = q1.popleft()
            if x == m - 1 and y == n - 1:
                break
            for nextx, nexty in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nextx < m and 0 <= nexty < n and not marked[nextx][nexty]:
                    marked[nextx][nexty] = True
                    if grid[nextx][nexty]:
                        q2.append((nextx, nexty))
                    else:
                        q1.append((nextx, nexty))
            if not q1:
                q1, q2 = q2, q1
                ans += 1
        return ans

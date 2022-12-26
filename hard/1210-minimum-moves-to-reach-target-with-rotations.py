'''
你还记得那条风靡全球的贪吃蛇吗？

我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。
蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。
蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。

每次移动，蛇可以这样走：

如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。

返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 -1。

 

示例 1：



输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
示例 2：

输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9
 

提示：

2 <= n <= 100
0 <= grid[i][j] <= 1
蛇保证从空单元格开始出发。
'''
from collections import deque
from typing import List
'''
[TOC]

# 思路
BFS

# 解题方法
> 用BFS向前走，需要小心判断当前状态和下一个状态。详见代码

# 复杂度
- 时间复杂度: 
>  $O(n^2)$

- 空间复杂度: 
> $O(2^(m*n))$
'''


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        marked, queue = set(), deque()
        ans, n = 0, len(grid)
        target = (n - 1, n - 2, n - 1, n - 1)
        queue.append((0, 0, 0, 1))
        marked.add((0, 0, 0, 1))
        while queue:
            size = len(queue)
            for _ in range(size):
                pos = queue.popleft()
                if pos == target:
                    return ans
                r1, c1, r2, c2 = pos
                if r1 == r2:  # 横向的蛇
                    # 向右移动
                    if c2 + 1 < n and grid[r2][c2 + 1] == 0 and (r2, c2, r2, c2 + 1) not in marked:
                        queue.append((r2, c2, r2, c2 + 1))
                        marked.add((r2, c2, r2, c2 + 1))
                    # 向下移动
                    if r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0 and (r2 + 1, c1, r2 + 1, c2) not in marked:
                        queue.append((r2 + 1, c1, r2 + 1, c2))
                        marked.add((r2 + 1, c1, r2 + 1, c2))
                    # 向下转向
                    if r2 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0 and (r1, c1, r2 + 1, c1) not in marked:
                        queue.append((r1, c1, r2 + 1, c1))
                        marked.add((r1, c1, r2 + 1, c1))
                else:  # 纵向的蛇
                    # 向右移动
                    if c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0 and (r1, c1 + 1, r2, c2 + 1) not in marked:
                        queue.append((r1, c1 + 1, r2, c2 + 1))
                        marked.add((r1, c1 + 1, r2, c2 + 1))
                    # 向下移动
                    if r2 + 1 < n and grid[r2 + 1][c2] == 0 and (r2, c1, r2 + 1, c2) not in marked:
                        queue.append((r2, c1, r2 + 1, c2))
                        marked.add((r2, c1, r2 + 1, c2))
                    # 向右转向
                    if c1 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0 and (r1, c1, r1, c1 + 1) not in marked:
                        queue.append((r1, c1, r1, c1 + 1))
                        marked.add((r1, c1, r1, c1 + 1))
            ans += 1
        return -1


s = Solution()
print(s.minimumMoves([[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0]]))
print(s.minimumMoves([[0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0]]))

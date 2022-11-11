'''
1293. 网格中的最短路径
困难
212
相关企业
给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。

 

示例 1：



输入： grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
示例 2：



输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
输出：-1
解释：我们至少需要消除两个障碍才能找到这样的路径。
 

提示：

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] 是 0 或 1
grid[0][0] == grid[m-1][n-1] == 0
'''

from collections import deque
from typing import List
'''
[TOC]

# 思路
BFS

# 解题方法
> 相比普通的BFS可以消除部分障碍，简单的对普通BFS进行改造，将当前剩余能消除数加入队列和marked哈希表
> 遇到障碍时，如果剩余消除数>0，将当前消除数-1，障碍所占据的单元格也可以加入队列

# 复杂度
- 时间复杂度: 
> $O(mnk)$

- 空间复杂度: 
> $O(mnk)$
'''


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue, marked = deque(), set()
        queue.append((0, 0, k))
        marked.add((0, 0, k))
        ans = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, remainder = queue.popleft()
                if x == m - 1 and y == n - 1:
                    return ans
                for nextx, nexty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nextx < m and 0 <= nexty < n:
                        if grid[nextx][nexty]:  # 遇到障碍，如果有剩余的消除数，且相同状态下障碍没有遍历过，进行遍历
                            if remainder and (nextx, nexty, remainder - 1) not in marked:
                                queue.append((nextx, nexty, remainder - 1))
                                marked.add((nextx, nexty, remainder - 1))
                        else:
                            if (nextx, nexty, remainder) not in marked:
                                queue.append((nextx, nexty, remainder))
                                marked.add((nextx, nexty, remainder))
            ans += 1
        return -1


s = Solution()
assert s.shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1) == 6
assert s.shortestPath(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1) == -1

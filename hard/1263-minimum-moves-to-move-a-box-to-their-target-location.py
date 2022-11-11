'''
1263. 推箱子
困难
92
相关企业
「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。

游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。

现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：

玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
地板用字符 '.' 表示，意味着可以自由行走。
墙用字符 '#' 表示，意味着障碍物，不能通行。 
箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
玩家无法越过箱子。
返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。

 

示例 1：



输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：3
解释：我们只需要返回推箱子的次数。
示例 2：

输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：-1
示例 3：

输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：5
解释：向下、向左、向左、向上再向上。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid 仅包含字符 '.', '#',  'S' , 'T', 以及 'B'。
grid 中 'S', 'B' 和 'T' 各只能出现一个。
'''
from collections import deque
from functools import lru_cache
from typing import List
'''
[TOC]

# 思路
BFS

# 解题方法
> 箱子向1个方向移动，需要满足3个条件，
> 1. 前面没有障碍
> 2. 后面有空间
> 3. 人能够移动到后面的空间（这个判断需要用BFS查找路径）
> 满足如上条件后，将箱子的新位置、人的位置加入队列和哈希表，进行BFS搜索

# 复杂度
- 时间复杂度: 
> $O(mn*4*mn)$，因为人只能位于箱子的4周，所以人和箱子位置的组合数是4*mn，然后每次前进都需要判断人是否能够移动到指定位置，这个也需要一次时间复杂度为O(mn)的BFS

- 空间复杂度: 
> $O(4mn)$，人和箱子位置的组合数是4*mn
'''


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        # 找到箱子和人的初始位置
        m, n = len(grid), len(grid[0])
        boxPos, playerPos, targetPos = None, None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    boxPos = (i, j)
                elif grid[i][j] == 'S':
                    playerPos = (i, j)
                elif grid[i][j] == 'T':
                    targetPos = (i, j)

        # 下面开始用BFS查找可能的路径
        queue, marked = deque(), set()
        queue.append((boxPos, playerPos))
        marked.add((boxPos, playerPos))
        ans = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                boxPos, playerPos = queue.popleft()
                if boxPos == targetPos:
                    return ans
                # 遍历box的4个前进方向
                for nextX, nextY, backX, backY in [(boxPos[0] + 1, boxPos[1], boxPos[0] - 1, boxPos[1]), (boxPos[0] - 1, boxPos[1], boxPos[0] + 1, boxPos[1]),
                                                   (boxPos[0], boxPos[1] + 1, boxPos[0], boxPos[1] - 1), (boxPos[0], boxPos[1] - 1, boxPos[0], boxPos[1] + 1)]:
                    # 前进位置和后面都有空间才可以
                    if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] != '#' and 0 <= backX < m and 0 <= backY < n and grid[backX][backY] != '#':
                        # 位置之前未遍历过，且人可以移动到箱子背后，那么将状态加入队列
                        if ((nextX, nextY), (backX, backY)) not in marked and self.canMove(boxPos, playerPos, (backX, backY)):
                            queue.append(((nextX, nextY), (backX, backY)))
                            marked.add(((nextX, nextY), (backX, backY)))
            ans += 1
        return -1

    # 判断人是否能够移动到指定位置
    @lru_cache
    def canMove(self, boxPos, srcPos, targetPos):  # 后3个参数分别是箱子的位置、人的起始位置、人的目标位置
        m, n = len(self.grid), len(self.grid[0])
        marked, queue = set(), deque()
        marked.add(srcPos)
        queue.append(srcPos)
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if (x, y) == targetPos:
                    return True
                for nextX, nextY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (nextX, nextY) == boxPos:  # 如果下一个位置是箱子，不可以
                        continue
                    if 0 <= nextX < m and 0 <= nextY < n and self.grid[nextX][nextY] != '#' and (nextX, nextY) not in marked:
                        queue.append((nextX, nextY))
                        marked.add((nextX, nextY))
        return False


s = Solution()
assert s.minPushBox([["#", "#", "#", "#", "#", "#", "#"], ["#", "S", "#", ".", "B", "T", "#"], ["#", "#", "#", "#", "#", "#", "#"]]) == -1
print(
    s.minPushBox(grid=[["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"],
                       ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]))
print(
    s.minPushBox(grid=[["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"], ["#", ".", ".", "B", ".", "#"], ["#", "#", "#", "#", ".", "#"],
                       ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]))
print(
    s.minPushBox([["#", "#", "#", "#", "#", "#"], ["#", "T", ".", ".", "#", "#"], ["#", ".", "#", "B", ".", "#"], ["#", ".", ".", ".", ".", "#"],
                  ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]))

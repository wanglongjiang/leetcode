'''
甲板上的战舰
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
进阶:

你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？
'''
from typing import List
'''
思路：一次扫描。
一次扫描，如果左、上没有相邻的X，可以认为是新的战舰。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                if row[j] == 'X':
                    if j == 0 or row[j - 1] != 'X':
                        if i == 0 or board[i - 1][j] != 'X':
                            count += 1
        return count


s = Solution()
print(s.countBattleships([['X', '.', '.', 'X'], ['X', '.', '.', '.'], ['X', '.', '.', '.']]))

'''
794. 有效的井字游戏
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。

示例 2:
输入: board = ["XOX", " X ", "   "]
输出: false
解释: 玩家应该是轮流放置的。

示例 3:
输入: board = ["XXX", "   ", "OOO"]
输出: false

示例 4:
输入: board = ["XOX", "O O", "XOX"]
输出: true
说明:

游戏板 board 是长度为 3 的字符串数组，其中每个字符串 board[i] 的长度为 3。
 board[i][j] 是集合 {" ", "X", "O"} 中的一个字符。
'''
from typing import List
from collections import Counter
'''
思路：按照游戏规则判断
根据游戏规则整理出的判断
1. x的数量等于o，或者x比o多1个
2. x与o不能同时有胜利局
3. 如果x胜利，它是先手，肯定会比o多1个
4. 如果o胜利，它是后手，双方的棋子一样多

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        counter = Counter()  # 统计x,o的个数
        counter.update(board[0])
        counter.update(board[1])
        counter.update(board[2])
        if counter['X'] < counter['O'] or counter['X'] - counter['O'] > 1:
            return False

        def isWin(x):
            for i in range(3):  # 遍历3行、3列
                if board[i] == x + x + x:  # 一行
                    return True
                if board[0][i] == board[1][i] == board[2][i] == x:  # 一列
                    return True
            if board[0][0] == board[1][1] == board[2][2] == x:  # 对角线
                return True
            if board[0][2] == board[1][1] == board[2][0] == x:  # 反对角线
                return True
            return False

        if isWin('X') and isWin('O'):  # 两个人不能同时胜利
            return False
        if isWin('X') and counter['X'] - counter['O'] != 1:  # 如果x胜利，它是先手，肯定比o多1个
            return False
        if isWin('O') and counter['X'] != counter['O']:  # 如果o胜利，它是后手，双方的棋子一样多
            return False
        return True


s = Solution()
print(s.validTicTacToe(["OXX", "XOX", "OXO"]) == False)
print(s.validTicTacToe(["XXX", "XOO", "OO "]) == False)
print(s.validTicTacToe(["O  ", "   ", "   "]))
print(s.validTicTacToe(["XOX", " X ", "   "]))
print(s.validTicTacToe(["XXX", "   ", "OOO"]))
print(s.validTicTacToe(["XOX", "O O", "XOX"]))
print(s.validTicTacToe(["   ", "   ", "   "]))

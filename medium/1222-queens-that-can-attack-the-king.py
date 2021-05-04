'''
可以攻击国王的皇后
在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。

「黑皇后」在棋盘上的位置分布用整数坐标数组 queens 表示，「白国王」的坐标用数组 king 表示。

「黑皇后」的行棋规定是：横、直、斜都可以走，步数不受限制，但是，不能越子行棋。

请你返回可以直接攻击到「白国王」的所有「黑皇后」的坐标（任意顺序）。

提示：

1 <= queens.length <= 63
queens[i].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
一个棋盘格上最多只能放置一枚棋子。
'''
from typing import List
'''
思路：模拟
从国王出发，沿8个方向前进，如果能遇到皇后，则将该皇后加入结果list,同时该方向不再继续前进，更换方向继续检查
时间复杂度：O(56)
空间复杂度：O(1)
'''


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queenPos = set()
        for queen in queens:
            queenPos.add(queen[0] * 8 + queen[1])
        directs = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1)]
        for direct in directs:
            pos = king.copy()
            while 0 <= pos[0] + direct[0] < 8 and 0 <= pos[1] + direct[1] < 8:
                pos[0] += direct[0]
                pos[1] += direct[1]
                if (pos[0] * 8 + pos[1]) in queenPos:
                    ans.append([pos[0], pos[1]])
                    break
        return ans


s = Solution()
print(s.queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
print(s.queensAttacktheKing(queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))
print(
    s.queensAttacktheKing(queens=[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1,
                                                                                                                                                   1], [6, 4],
                                  [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1],
                                  [0, 6], [4, 3], [1, 7]],
                          king=[3, 4]))

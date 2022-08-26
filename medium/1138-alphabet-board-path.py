'''
1138. 字母板上的路径
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。



我们可以按下面的指令规则行动：

如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

 

示例 1：

输入：target = "leet"
输出："DDR!UURRR!!DDD!"
示例 2：

输入：target = "code"
输出："RR!DDRR!UUL!R!"
 

提示：

1 <= target.length <= 100
target 仅含有小写英文字母。
'''
'''
思路：哈希 模拟
记住每个字符的下标，然后遍历target，计算当前坐标与字符的坐标的差，输出纵、横坐标上需要移动的指令。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # 计算每个字符的坐标
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos[board[i][j]] = (i, j)
        # 定义上下、左右移动函数
        def moveUD(char):
            if pos[char][0] > cur[0]:
                ans.append('D' * abs(pos[char][0] - cur[0]))
            elif pos[char][0] < cur[0]:
                ans.append('U' * abs(pos[char][0] - cur[0]))

        def moveLR(char):
            if pos[char][1] > cur[1]:
                ans.append('R' * abs(pos[char][1] - cur[1]))
            elif pos[char][1] < cur[1]:
                ans.append('L' * abs(pos[char][1] - cur[1]))

        cur, ans = (0, 0), []
        for char in target:
            if char == 'z':  # 目标是'z'，需要特殊处理，必须先向左移动，然后才能向下，否则会越过边界
                moveLR(char)
                moveUD(char)
            else:
                moveUD(char)
                moveLR(char)
            ans.append('!')
            cur = pos[char]  # 修改当前坐标
        return ''.join(ans)

'''
2116. 判断一个括号字符串是否有效
一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的：

字符串为 ().
它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。
它可以表示为 (A) ，其中 A 是一个有效括号字符串。
给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。locked 是一个二进制字符串，只包含 '0' 和 '1' 。对于 locked 中 每一个 下标 i ：

如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。
如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。
如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。

 

示例 1：



输入：s = "))()))", locked = "010100"
输出：true
解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。
我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。
示例 2：

输入：s = "()()", locked = "0000"
输出：true
解释：我们不需要做任何改变，因为 s 已经是有效字符串了。
示例 3：

输入：s = ")", locked = "0"
输出：false
解释：locked 允许改变 s[0] 。
但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。
 

提示：

n == s.length == locked.length
1 <= n <= 105
s[i] 要么是 '(' 要么是 ')' 。
locked[i] 要么是 '0' 要么是 '1' 。
'''
'''
思路：栈
设一个栈，内部保存2种元素，第1种是'('，第2种是数字，也就是通用匹配符的数量
遍历s，
如果locked为1，
- 如果s[i]为')'，需要出栈一个'('或者通用匹配符进行匹配，优先使用'('，找不到'('才会使用通用匹配符
- 如果s[i]为'('，入栈
如果locked为0，
- 将通用匹配符的数量1入栈，如果栈顶就是一个通用匹配符的数量，将2个数量进行合并

最后遍历栈，不断出栈，遇到'('，通用匹配数+1，否则通用匹配数+上出栈的数量。这个过程中通用匹配数量不能<0。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:  # 长度为奇数，肯定无法匹配
            return False
        stk = []
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    stk.append('(')
                elif stk:
                    if stk[-1] == '(':  # 栈顶是'('，可以与当前右括号匹配
                        stk.pop()
                    else:  # 栈顶是通用匹配，向下寻找一个'('进行匹配
                        starNum = stk.pop()
                        if stk:  # 因为通用匹配入栈的时候会进行合并，所以通用匹配下面的肯定是左括号，可以匹配掉
                            stk.pop()
                        else:  # 没有可以使用的左括号，用掉一个通用匹配
                            starNum -= 1
                        if stk and stk[-1] != '(':
                            stk[-1] += starNum  # 通用匹配进行合并
                        elif starNum:
                            stk.append(starNum)  # 不能合并，入栈
                else:  # 右括号找不到能匹配的，返回false
                    return False
            else:
                if not stk or stk[-1] == '(':
                    stk.append(1)  # 将1个通用匹配入栈
                else:
                    stk[-1] += 1  # 栈顶的通用匹配+1
        starNum = 0
        while stk:
            if stk[-1] == '(':
                starNum -= 1
                stk.pop()
            else:
                starNum += stk.pop()
            if starNum < 0:
                return False
        return True


s = Solution()
print(s.canBeValid("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))
print(s.canBeValid("((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"))
print(s.canBeValid(s="))()))", locked="010100"))
print(s.canBeValid(s="()()", locked="0000"))
print(s.canBeValid(s=")", locked="0"))

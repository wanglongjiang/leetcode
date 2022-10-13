'''
1541. 平衡括号字符串的最少插入次数
给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：

任何左括号 '(' 必须对应两个连续的右括号 '))' 。
左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。

你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。

请你返回让 s 平衡的最少插入次数。

 

示例 1：

输入：s = "(()))"
输出：1
解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))" 。
示例 2：

输入：s = "())"
输出：0
解释：字符串已经平衡了。
示例 3：

输入：s = "))())("
输出：3
解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
示例 4：

输入：s = "(((((("
输出：12
解释：添加 12 个 ')' 得到平衡字符串。
示例 5：

输入：s = ")))))))"
输出：5
解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
 

提示：

1 <= s.length <= 10^5
s 只包含 '(' 和 ')' 。
'''
'''
思路：栈
遇到'('，stk+1
遇到连续的'))'，尝试出栈(stk-1)，如果不存在，则将答案+1
遇到单独的')'，答案+2


时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minInsertions(self, s: str) -> int:
        ans, stk = 0, 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                stk += 1
                i += 1
            elif i < n - 1:
                if s[i + 1] == ')':  # 遇到'))'
                    if stk:  # 能够匹配
                        stk -= 1
                    else:  # 不能匹配，需要在前面添加'('
                        ans += 1
                    i += 2
                else:  # 遇到')('
                    if stk:
                        ans += 1
                        stk -= 1
                    else:
                        ans += 2
                    i += 1
            else:  # 遇到单独的')'
                if stk:
                    ans += 1
                    stk -= 1
                else:
                    ans += 2
                i += 1
        ans += stk * 2
        return ans


s = Solution()
assert s.minInsertions("))())(") == 3
assert s.minInsertions("(()))") == 1
assert s.minInsertions("())") == 0
assert s.minInsertions("((((((") == 12
assert s.minInsertions(")))))))") == 5
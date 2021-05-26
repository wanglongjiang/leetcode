'''
使括号有效的最少添加
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

它是一个空字符串，或者
它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
它可以被写作 (A)，其中 A 是有效字符串。
给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

 

示例 1：

输入："())"
输出：1
示例 2：

输入："((("
输出：3
示例 3：

输入："()"
输出：0
示例 4：

输入："()))(("
输出：4
 

提示：

S.length <= 1000
S 只包含 '(' 和 ')' 字符。
'''
'''
思路：栈
遇到'('入栈，遇到')'尝试出栈，如果栈为空，则+1
最后统计栈的大小
优化空间复杂度，因入栈的只有'('，可以使用一个整数变量记录栈的大小，不需要真正入栈

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        missCount = 0
        stackSize = 0
        for c in s:
            if c == '(':
                stackSize += 1
            else:
                if stackSize > 0:
                    stackSize -= 1
                else:
                    missCount += 1
        missCount += stackSize
        return missCount


s = Solution()
print(s.minAddToMakeValid("())"))
print(s.minAddToMakeValid("((("))
print(s.minAddToMakeValid("()"))
print(s.minAddToMakeValid("()))(("))

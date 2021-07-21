'''
括号的分数

给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50
'''
'''
思路：栈
遇到(入栈，
遇到)先查看栈顶元素：
    如果栈顶元素是(，说明2个括弧之间没有其他内容，将当前值计数为1，入栈
    如果栈顶元素不是(，需要持续出栈将(到栈顶的元素相加，然后*2，值入栈
最后将栈内元素相加
'''


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                val = 0
                while stack[-1] != '(':
                    val += stack.pop()
                stack.pop()
                stack.append(val * 2)
        return sum(stack)


s = Solution()
print(s.scoreOfParentheses("()"))
print(s.scoreOfParentheses("(())"))
print(s.scoreOfParentheses("()()"))
print(s.scoreOfParentheses("(()(()))"))

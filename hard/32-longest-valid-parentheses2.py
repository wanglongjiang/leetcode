'''
最长有效括号

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

'''
'''
思路：栈顶放最近匹配不成功的右括弧的下标，初始放-1
遍历字符串，遇到左括号入栈下标，遇到右括号出栈，每个匹配成功的右括号与栈顶的差即为该右括号的长度
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        maxLen = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxLen = max(maxLen, i - stack[len(stack) - 1])
                else:
                    stack.append(i)
        return maxLen


s = Solution()
print(s.longestValidParentheses("(((((())(()))))"))
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))
print(s.longestValidParentheses("(((((())(())(((((((()))"))

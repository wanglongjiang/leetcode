'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif ch == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif ch == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))

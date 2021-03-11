'''
逆波兰表达式求值
根据 逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

 

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
'''
from typing import List
'''
思路：遇到操作数入栈，遇到操作符出栈运算，最后返回栈底元素即为结果
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op == '+':
                stack.append(stack.pop() + stack.pop())
            elif op == '-':
                stack.append(-stack.pop() + stack.pop())
            elif op == '*':
                stack.append(stack.pop() * stack.pop())
            elif op == '/':
                n = stack.pop()
                stack.append(int(stack.pop() / n))
            else:
                stack.append(int(op))
        return stack[-1]


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

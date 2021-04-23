'''
面试题 16.26. 计算器
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''
'''
思路：双栈计算法
运算符有优先级，
    遇到整数入栈
    遇到+，-入栈
    遇到*，/，出栈1个数，与后面的数进行计算，然后入栈
'''


class Solution:
    def calculate(self, s: str) -> int:
        operator, operands = [], []  # 操作符，操作数 2个栈
        i, n = 0, len(s)

        def nextToken():
            nonlocal i
            while i < n:
                if s[i].isdigit():
                    j = i + 1
                    while j < n and s[j].isdigit():
                        j += 1
                    num = int(s[i:j])
                    i = j
                    return num
                elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                    i += 1
                    return s[i - 1]
                i += 1
            return None

        # 将*/计算完
        token = nextToken()
        while token is not None:
            if token == '+' or token == '-':
                operator.append(token)
            elif token == '*':
                num1 = operands.pop()
                operands.append(num1 * nextToken())
            elif token == '/':
                num1 = operands.pop()
                operands.append(int(num1 / nextToken()))
            else:
                if operator and operator[-1] == '-':  # 将-的下一个操作数改为负数
                    operands.append(-token)
                    operator[-1] = '+'
                else:
                    operands.append(token)
            token = nextToken()
        # 将+-计算完
        while operator:
            operator.pop()
            operands.append(operands.pop() + operands.pop())

        return operands[0]


s = Solution()
print(s.calculate("14-3/2"))
print(s.calculate("3+2*2"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate(" 5-3+5 "))

'''
基本计算器 II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。
1 <= s.length <= 3 * 10^5
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 23^1 - 1] 内
题目数据保证答案是一个 32-bit 整数

'''
'''
思路：编译原理里面的自顶向下语法分析。
因为运算符有优先级，采用自顶向下的语法分析方法，输出逆波兰式进行计算
'''


# 词法分析
class Lexer:
    def __init__(self, s: str):
        self.s = s
        self.i = 0
        self.op = None
        self.lookahead = None

    def lexan(self):
        while self.i < len(self.s):
            ch = self.s[self.i]
            if ch.isdigit():
                while self.i + 1 < len(self.s) and self.s[self.i + 1].isdigit():
                    self.i += 1
                    ch += self.s[self.i]
                self.op = int(ch)
                self.lookahead = 'num'
                self.i += 1
                return
            elif ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '(' or ch == ')':
                self.lookahead = ch
                self.i += 1
                return
            self.i += 1
        self.lookahead = 'end'


class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        lexer = Lexer(s)

        # 自顶向下的语法分析
        def expr():
            mul_term()
            while True:
                if lexer.lookahead == '+' or lexer.lookahead == '-':
                    lookahead = lexer.lookahead
                    match(lookahead)
                    mul_term()
                    ops.append(lookahead)
                else:
                    return

        def mul_term():
            term()
            while True:
                if lexer.lookahead == '*' or lexer.lookahead == '/':
                    lookahead = lexer.lookahead
                    match(lookahead)
                    term()
                    ops.append(lookahead)
                else:
                    return

        def term():
            if lexer.lookahead == '(':
                match('(')
                expr()
                match(')')
            elif lexer.lookahead == 'num':
                ops.append(lexer.op)
                match('num')

        def match(ch):
            if lexer.lookahead == ch:
                lexer.lexan()
            else:
                raise Exception('表达式错误:%s' % ch)

        # 分析表达式，并将逆波兰式输出到ops
        lexer.lexan()
        while lexer.lookahead != 'end':
            expr()
        match('end')
        # 执行表达式
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack.pop() + stack.pop())
            elif op == '-':
                stack.append(-stack.pop() + stack.pop())
            elif op == '*':
                stack.append(stack.pop() * stack.pop())
            elif op == '/':
                n = stack.pop()
                stack.append(stack.pop() // n)
            else:
                stack.append(op)
        return stack[-1]


s = Solution()
print(s.calculate(" 3-2 "))
print(s.calculate(" 3/2 "))
print(s.calculate("3+2*2"))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate(" (3+5) / 2 "))

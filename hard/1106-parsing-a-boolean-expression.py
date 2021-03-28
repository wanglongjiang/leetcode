'''
解析布尔表达式
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

有效的表达式需遵循以下约定：

"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）

提示：
1 <= expression.length <= 20000
expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
expression 是以上述形式给出的有效表达式，表示一个布尔值。
'''
'''
思路：栈。
表达式为逆波兰式，采用双栈算法。
遍历表达式，
    遇到操作符入栈，
    遇到左括号入栈，
    遇到操作数入栈，
    遇到右括号，弹出1个操作符，再弹出操作数直至遇到左括号，计算操作数与操作符的运算结果，将结果入栈
遍历完成后，操作数栈栈顶元素即为结果
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        opr, ops = [], []
        for c in expression:
            if c == '|' or c == '&' or c == '!':
                opr.append(c)
            elif c == 't':
                ops.append(True)
            elif c == 'f':
                ops.append(False)
            elif c == '(':
                ops.append('(')
            elif c == ')':
                op = opr.pop()
                if op == '&':
                    v = ops.pop()
                    while ops[-1] != '(' and v:  # 如果v已经为false，后面不需要再计算
                        v = v and ops.pop()
                    while ops[-1] != '(':  # 跳过短路表达式
                        ops.pop()
                    ops.pop()  # 弹出左括号
                    ops.append(v)
                elif op == '|':
                    v = ops.pop()
                    while ops[-1] != '(' and not v:  # 如果v已经为true，后面不需要再计算
                        v = v or ops.pop()
                    while ops[-1] != '(':  # 跳过短路表达式
                        ops.pop()
                    ops.pop()  # 弹出左括号
                    ops.append(v)
                else:
                    v = ops.pop()
                    ops.pop()  # 弹出左括号
                    ops.append(not v)
        return ops[-1]


s = Solution()
print(s.parseBoolExpr("!(f)"))
print(s.parseBoolExpr("|(f,t)"))
print(s.parseBoolExpr("&(t,f)"))
print(s.parseBoolExpr("|(&(t,f,t),!(t))"))

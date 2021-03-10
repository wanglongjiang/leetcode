'''
基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
'''
'''
思路1：经典的双栈方法基本计算器
1个栈numStk存放数字，另外1栈funStk存放操作数
遍历输入字符串，
    如果是数字，numStk入栈，如果操作数多于1个且操作符不是括号，可以进行计算
    如果是+、-，funStk入栈。
        输入的字符串中有负号，需要特殊处理
    如果是右括号')'，弹出funStk中的函数，与numStk中的2个操作数进行计算，然后计算结果入栈，
        持续该过程直至遇到左括号'('，把括号内表达式计算完毕
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def calculate(self, s: str) -> int:
        numStk = []
        funStk = []

        # 根据栈顶函数和操作数进行计算
        def calc():
            while funStk and funStk[-1] != '(':
                func = funStk[-1]
                if func == 'neg':  # 符号
                    funStk.pop()
                    numStk.append(-numStk.pop())
                elif func == '+':
                    if len(numStk) >= 2:
                        funStk.pop()
                        numStk.append(numStk.pop() + numStk.pop())
                    else:
                        break
                elif func == '-':
                    if len(numStk) >= 2:
                        funStk.pop()
                        numStk.append(-numStk.pop() + numStk.pop())
                    else:
                        break

        i = 0
        preOp = None  # 前一个操作
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                while i + 1 < len(s) and s[i + 1].isdigit():
                    i += 1
                    ch += s[i]
                numStk.append(int(ch))
                calc()
            elif ch == '+':
                funStk.append(ch)
            elif ch == '-':
                if preOp is None or preOp == '+' or preOp == '-' or preOp == '(':  # 负号前面没有其他操作数
                    funStk.append('neg')
                else:
                    funStk.append(ch)
            elif ch == '(':
                funStk.append(ch)
            elif ch == ')':
                calc()
                funStk.pop()
                calc()  # 括号内表达式计算完成后，与前面的表达式可能还可以继续计算
            i += 1
            preOp = ch
        while funStk:
            calc()
        return numStk[-1]


s = Solution()
print(s.calculate("(7)-(0)+(4)"))
print(s.calculate("-2+ 1"))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
print(s.calculate("2147483647"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("1 + 1"))

'''
为运算表达式设计优先级
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

'''
from typing import List
'''
思路：分治
将表达式从某个运算符op分成左右2部分，先分别计算得到左半部分的运算结果集leftset，右半部分的运算结果集rightset
该表达式的运算结果集为leftset中和rightset中分别拿出1个元素的组合，用op进行计算的结果
'''


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        func = {}
        func['+'] = lambda a, b: a + b
        func['-'] = lambda a, b: a - b
        func['*'] = lambda a, b: a * b
        # 将表达式分解为操作符，操作数
        opr, opd = [], []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                j = i + 1
                while j < n and expression[j].isdigit():
                    j += 1
                opd.append(int(expression[i:j]))
                i = j
            else:
                opr.append(expression[i])
                i += 1
        if not opr:
            return opd

        # 从任意操作符处开始分治
        def dc(i, j):
            if i == j:
                return [func[opr[i]](opd[i], opd[i + 1])]
            elif j - i == 1:
                res1 = func[opr[j]](func[opr[i]](opd[i], opd[i + 1]), opd[j + 1])
                res2 = func[opr[i]](opd[i], func[opr[j]](opd[j], opd[j + 1]))
                return [res1, res2]
            else:
                ans = []
                for k in range(i, j + 1):
                    if k == i:
                        set1 = [opd[k]]
                    else:
                        set1 = dc(i, k - 1)
                    if k == j:
                        set2 = [opd[k + 1]]
                    else:
                        set2 = dc(k + 1, j)
                    for s1 in set1:
                        for s2 in set2:
                            ans.append(func[opr[k]](s1, s2))
                return ans

        ans = dc(0, len(opr) - 1)
        return ans


s = Solution()
print(s.diffWaysToCompute("2-1-1"))
print(s.diffWaysToCompute("2*3-4*5"))

'''
求解方程

求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。

如果方程没有解，请返回“No solution”。

如果方程有无限解，则返回“Infinite solutions”。

如果方程中只有一个解，要保证返回值 x 是一个整数。

示例 1：

输入: "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: "x=x"
输出: "Infinite solutions"
示例 3:

输入: "2x=x"
输出: "x=0"
示例 4:

输入: "2x+3x-6x=x+2"
输出: "x=-1"
示例 5:

输入: "x=x+2"
输出: "No solution"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/solve-the-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import re
'''
思路：模拟
将变量x集中到表达式左侧，数值集中到表达式右侧。
然后右侧表达式除以左侧x的系数，得到x的值
如果左侧系数为0，右侧值也为0，有无限解
如果左侧系数为0，右侧不为0，无解

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def solveEquation(self, equation: str) -> str:
        coef, val = 0, 0
        left, neg = True, False
        formula = list(filter(None, re.split(r'(x)|(\d+)|(\=)|(\+)|(\-)', equation)))
        formula.reverse()
        while formula:
            a = formula.pop()
            if a.isdigit():
                if formula and formula[-1] == 'x':
                    formula.pop()
                    if left:
                        coef += -int(a) if neg else int(a)
                    else:
                        coef += int(a) if neg else -int(a)
                else:
                    if left:
                        val += int(a) if neg else -int(a)
                    else:
                        val += -int(a) if neg else int(a)
                neg = False
            elif a == '+':
                pass
            elif a == '-':
                neg = True
            elif a == 'x':
                if left:
                    coef += -1 if neg else 1
                else:
                    coef -= -1 if neg else 1
                neg = False
            elif a == '=':
                left = False
        if coef == 0 and val != 0:
            return 'No solution'
        if coef == 0 and val == 0:
            return 'Infinite solutions'
        return 'x=' + str(int(val / coef))


s = Solution()
print(s.solveEquation('-x=1'))
print(s.solveEquation('2x+3x-6x=x+2'))
print(s.solveEquation('x+5-3+x=6+x-2'))
print(s.solveEquation('x=x'))
print(s.solveEquation('2x=x'))
print(s.solveEquation('x=x+2'))

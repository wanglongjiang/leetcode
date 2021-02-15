'''

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
'''
'''
思路：设n=0..31，通过divisor加倍的方式将构造一个divisor*2^n表格tab，
表格最后2个元素有tab[n-1]=divisor*2^(n-1)<dividend<=divisor*2^n
表格从最高项开始与dividend比较，如果tab[i]<=dividend，将dividend=dividend-tab[i],将2^i累加到商里面
最后直到dividend为零，或者小于divisor。
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 为防止计算过程中溢出，进行特殊处理
        if divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend == -2**31:
                return 2**31 - 1
            else:
                return -dividend
        elif divisor == dividend:
            return 1
        elif divisor == -2**31:
            return 0
        # 设置结果正负符号
        negative = False
        quotient = 0
        if dividend < 0:
            if divisor > 0:
                negative = True
            else:
                divisor = abs(divisor)
            # 为防止abs(diviend)溢出，将其减去abs(divisor)
            if dividend == -2**31:
                dividend += abs(divisor)
                quotient = 1
            dividend = abs(dividend)
        elif dividend > 0 and divisor < 0:
            negative = True
            divisor = abs(divisor)
        tab = [divisor]
        while tab[len(tab) - 1] < dividend:
            tab.append(tab[len(tab) - 1] << 1)
        for i in range(len(tab) - 1, -1, -1):
            if tab[i] <= dividend:
                dividend -= tab[i]
                quotient += 1 << i
        return quotient if not negative else -quotient


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))

'''
坏了的计算器
在显示着数字的坏计算器上，我们可以执行以下两种操作：

双倍（Double）：将显示屏上的数字乘 2；
递减（Decrement）：将显示屏上的数字减 1 。
最初，计算器显示数字 X。

返回显示数字 Y 所需的最小操作数。
'''
'''
思路：折半。
如果X比Y大，只能递减。
如果X比Y小，可以将Y折半，然后继续对比X与Y，直至X=Y或者X>Y,执行递减
'''


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        step = 0
        while Y > X:
            step += 1
            Y >>= 1
        if X > Y:
            step += X - Y
        return step

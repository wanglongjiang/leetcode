'''
剑指 Offer II 001. 整数除法

给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

 

注意：

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231−1]。本题中，如果除法结果溢出，则返回 231 − 1
 

示例 1：

输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7
示例 2：

输入：a = 7, b = -3
输出：0
解释：7/-3 = truncate(-2.33333..) = -2
示例 3：

输入：a = 0, b = 1
输出：0
示例 4：

输入：a = 1, b = 1
输出：1
 

提示:

-2^31 <= a, b <= 231 - 1
b != 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xoh6Oh
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
思路：设n=0..31，通过divisor加倍的方式将构造一个divisor*2^n表格tab，
表格最后2个元素有tab[n-1]=divisor*2^(n-1)<dividend<=divisor*2^n
表格从最高项开始与dividend比较，如果tab[i]<=dividend，将dividend=dividend-tab[i],将2^i累加到商里面
最后直到dividend为零，或者小于divisor。

时间复杂度：O(loga)
空间复杂度：O(loga)
'''


class Solution:
    def divide(self, a: int, b: int) -> int:
        # 为防止计算过程中溢出，进行特殊处理
        if b == 1:
            return a
        elif b == -1:
            if a == -2**31:
                return 2**31 - 1
            else:
                return -a
        elif b == a:
            return 1
        elif b == -2**31:
            return 0
        # 设置结果正负符号
        negative = False
        quotient = 0
        if a < 0:
            if b > 0:
                negative = True
            else:
                b = abs(b)
            # 为防止abs(diviend)溢出，将其减去abs(b)
            if a == -2**31:
                a += abs(b)
                quotient = 1
            a = abs(a)
        elif a > 0 and b < 0:
            negative = True
            b = abs(b)
        tab = [b]
        while tab[len(tab) - 1] < a:
            tab.append(tab[len(tab) - 1] << 1)
        for i in range(len(tab) - 1, -1, -1):
            if tab[i] <= a:
                a -= tab[i]
                quotient += 1 << i
        return quotient if not negative else -quotient


s = Solution()
print(s.divide(a=15, b=2))
print(s.divide(a=7, b=-3))

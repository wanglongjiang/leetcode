'''
复数乘法
给定两个表示复数的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:

输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
示例 2:

输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
注意:

输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。

'''
'''
思路：模拟
按照复数相乘的数学公式计数出结果
(rn1+in1)*(rn2+in2) = rn1*rn2+(rn1*in2+rn2*in1)i+in1*in2*i^2= rn1*rn2-in1*in2 + (rn1*in2+rn2*in1)i

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        c1 = num1.replace('i', '').split('+')
        c2 = num2.replace('i', '').split('+')
        rn1, in1 = int(c1[0]), int(c1[1])
        rn2, in2 = int(c2[0]), int(c2[1])
        rn = rn1 * rn2 - in1 * in2
        inum = rn1 * in2 + rn2 * in1
        s1 = str(rn)
        s2 = str(inum) + 'i'
        return s1 + '+' + s2


s = Solution()
print(s.complexNumberMultiply("1+1i", "1+1i"))
print(s.complexNumberMultiply("1+-1i", "1+-1i"))

'''
剑指 Offer 43. 1～n 整数中 1 出现的次数

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6
 

限制：

1 <= n < 2^31
注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/
'''
'''
思路：数学

'''


class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, i = 0, 1
        while i <= n:
            ans += n // (i * 10) * i
            x = (n // i) % 10
            ans += i if x > 1 else (n % i + 1) * x
            i *= 10
        return ans

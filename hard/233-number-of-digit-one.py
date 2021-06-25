'''
数字 1 的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例 1：

输入：n = 13
输出：6
示例 2：

输入：n = 0
输出：0
'''
'''
思路：数字规律。

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

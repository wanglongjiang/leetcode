'''
600. 不含连续1的非负整数
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 10^9
'''
'''
思路：数学

'''


class Solution:
    def findIntegers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        bits = 0
        while n >> bits:
            bits += 1
        if (n >> (bits - 2)) == 3:
            return self.fib(bits)
        else:
            return self.fib(bits - 1) + self.findIntegers(n & ((1 << (bits - 1)) - 1))

    def fib(self, n):
        if n <= 0:
            return 1
        if n == 1:
            return 2
        a, b, c = 1, 2, 3
        i = n - 2
        while i:
            i -= 1
            a, b = b, c
            c = a + b
        return c


s = Solution()
print(s.findIntegers(6))

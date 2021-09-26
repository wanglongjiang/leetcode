'''
剑指 Offer 44. 数字序列中某一位的数字

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
'''
'''
思路：数学
先观察数字规律
小于10，1~9，9个数字，9位
小于100，10~99，90个数字，180位
小于1000，100~999，900个数字，2700位

各个区间的下限上限是[0,10),[10, 100),[100,1000)...位数是1，2，3...
从第1个区间的上限开始进行比较，如果大于上限，将上下限*10，将n=n-(上限-下限)*位数 直至找到n所在的区间
找到区间后，n/位数 找到所在的数字，然后n%位数，找到数字的第几位数字
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        digitCount = 1
        bottom, top = 0, 10
        while n > (top - bottom) * digitCount:
            n -= (top - bottom) * digitCount
            digitCount += 1
            bottom, top = top, top * 10
        num, r = divmod(n, digitCount)
        return int(str(num + bottom)[r])

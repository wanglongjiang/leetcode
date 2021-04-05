'''
第 N 位数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。

 

注意：n 是正数且在 32 位整数范围内（n < 231）。
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


s = Solution()
print(s.findNthDigit(2147483647))
print(s.findNthDigit(1))
print(s.findNthDigit(3))
print(s.findNthDigit(10))
print(s.findNthDigit(11))
print(s.findNthDigit(100))

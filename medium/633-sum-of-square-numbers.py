'''
平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
提示：

0 <= c <= 23^1 - 1
'''
'''
思路：数学+暴力搜索
从数学中知道如果c%4==3，不是完全平方数
如果不满足上面的条件，继续用暴力计算进行判定，从0..sqrt(c)开始，尝试每个数对的组合
时间复杂度：O(sqrt(c))
空间复杂度：O(1)
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        end = int(c**0.5)
        if end * end == c:
            return True
        if c % 4 == 3:
            return False
        a = 0
        while a <= end:
            num = a * a + end * end
            if num == c:
                return True
            elif num > c:
                end -= 1
            else:
                a += 1
        return False


s = Solution()
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(4))
print(s.judgeSquareSum(1))

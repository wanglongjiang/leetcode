'''
给你一个整数 x ，如果 x 是一个回文整数，返回 ture ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10


s = Solution()
print(s.isPalindrome(2))
print(s.isPalindrome(22))
print(s.isPalindrome(232))
print(s.isPalindrome(2332))
print(s.isPalindrome(-232))
print(s.isPalindrome(-22))

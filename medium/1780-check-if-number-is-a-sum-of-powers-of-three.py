'''
判断一个数字是否可以表示成三的幂的和
给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。

提示：

1 <= n <= 107
'''
'''
思路：数学
依次减去3的幂(从log(n,3)开始)，如果能减到0，则为true

时间复杂度：O(log(n))
空间复杂度：O(1)
'''

from math import log


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(int(log(n, 3)), -1, -1):
            if 3**i <= n:
                n -= 3**i
        return n == 0


s = Solution()
assert s.checkPowersOfThree(12)
assert s.checkPowersOfThree(91)
assert s.checkPowersOfThree(21) == False

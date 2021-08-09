'''
超级丑数
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。
'''
from typing import List
'''
思路：动态规划
使用与264.[丑数 II](medium/264-ugly-number-ii.py)类似的思路

时间复杂度：O(mn)，m=len(primes)
空间复杂度：O(m+n)
'''


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        p = [0] * len(primes)  # 保存prime[i]指向dp的指针
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(prime * dp[index] for prime, index in zip(primes, p))
            for j in range(len(primes)):
                if dp[i] == primes[j] * dp[p[j]]:
                    p[j] += 1
        return dp[n - 1]


s = Solution()
print(s.nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))

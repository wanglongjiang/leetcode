'''
n 的第 k 个因子
给你两个正整数 n 和 k 。

如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。

考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。

'''
'''
思路：从小到大迭代
从1到n查找因子
时间复杂度：O(n)
'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                if k == 1:
                    return i
                else:
                    k -= 1
        return -1


s = Solution()
print(s.kthFactor(24, 6))
print(s.kthFactor(2, 2))
print(s.kthFactor(n=12, k=3))
print(s.kthFactor(n=7, k=2))
print(s.kthFactor(n=4, k=4))
print(s.kthFactor(n=1, k=1))
print(s.kthFactor(n=1000, k=3))
print(s.kthFactor(1, 1))
print(s.kthFactor(1, 2))

'''
2507. 使用质因数之和替换后可以取到的最小值
中等
8
相关企业
给你一个正整数 n 。

请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。

注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
返回 n 可以取到的最小值。

 

示例 1：

输入：n = 15
输出：5
解释：最开始，n = 15 。
15 = 3 * 5 ，所以 n 替换为 3 + 5 = 8 。
8 = 2 * 2 * 2 ，所以 n 替换为 2 + 2 + 2 = 6 。
6 = 2 * 3 ，所以 n 替换为 2 + 3 = 5 。
5 是 n 可以取到的最小值。
示例 2：

输入：n = 3
输出：3
解释：最开始，n = 3 。
3 是 n 可以取到的最小值。
 

提示：

2 <= n <= 105
'''
'''
[TOC]

# 思路
模拟

# 解题方法
模拟题意，找n的质因数，直至最后的结果为质数或者质因数之和不变

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def smallestValue(self, n: int) -> int:
        # 查找n的质因数数组，如果已经是质数，返回空数组
        def getPrimeFactors(n):
            factors = []
            for a in range(2, n // 2 + 1):
                while n % a == 0:
                    n //= a
                    factors.append(a)
                if n == 1:
                    break
            return factors

        while (fs := getPrimeFactors(n)):
            newn = sum(fs)
            if newn == n:
                break
            n = newn
        return n


s = Solution()
assert s.smallestValue(4) == 4
assert s.smallestValue(15)

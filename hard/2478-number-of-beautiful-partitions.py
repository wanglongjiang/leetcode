'''
2478. 完美分割的方案数
困难
14
相关企业
给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。

如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：

s 被分成 k 段互不相交的子字符串。
每个子字符串长度都 至少 为 minLength 。
每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。
质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。

一个 子字符串 是字符串中一段连续字符串序列。

 

示例 1：

输入：s = "23542185131", k = 3, minLength = 2
输出：3
解释：存在 3 种完美分割方案：
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
示例 2：

输入：s = "23542185131", k = 3, minLength = 3
输出：1
解释：存在一种完美分割方案："2354 | 218 | 5131" 。
示例 3：

输入：s = "3312958", k = 3, minLength = 1
输出：1
解释：存在一种完美分割方案："331 | 29 | 58" 。
 

提示：

1 <= k, minLength <= s.length <= 1000
s 每个字符都为数字 '1' 到 '9' 之一。
'''
'''
[TOC]

# 思路
动态规划

# 解题方法
设二维数组dp[k][n]，dp[i][j]意识是截止第i个分组，以s[j]为结尾的方案数。
状态转移方程为：
> dp[i][j] = sum(dp[i-1][0..j-minlength])，且需要满足s[j]为合数、s[j+1]为质数

因为k、n大小为1000，为了避免超时，需要计算dp每行数据的前缀和。

通过状态转移方程可以看出，一个状态只依赖于上一个切分，所以还可以优化空间为O(n)


# 复杂度
- 时间复杂度: 
> $O(kn)$ 

- 空间复杂度: 
> $O(n)$，可以优化空间为O(n)
'''


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        if n < k * minLength:  # 不满足最小长度要求
            return 0
        primes = {'2', '3', '5', '7'}
        if s[0] not in primes or s[-1] in primes:  # 第0个字符需要是质数，最后一个需要是合数
            return 0
        if k == 1:  # 切分成1个字符串，只有1种方法
            return 1
        # 先预处理一下，找到所有是合数，后面是质数的索引
        legalIndexs = set()
        for i in range(1, n - 1):
            if s[i] not in primes and s[i + 1] in primes:
                legalIndexs.add(i)
        if s[-1] not in primes:
            legalIndexs.add(n - 1)
        # 初始化第1个切分
        dp = [0] * n
        for i in filter(lambda i: i in legalIndexs, range(minLength - 1, n - (k - 1) * minLength)):  # 需要给后面的子串留出空间，第1个子串的末尾最大是n-(k-1)*minLength
            dp[i] = 1
        pres = [0] * n  # 前缀和数组
        for i in range(minLength - 1, n):
            pres[i] = pres[i - 1] + dp[i]
        # 开始dp处理
        for i in range(1, k - 1):  # 处理第1...k-2，因为最后一个切分肯定是以n-1结尾，不需要计算
            newdp = [0] * n
            for j in filter(lambda j: j in legalIndexs, range(minLength * (i + 1) - 1, n - (k - i - 1) * minLength)):
                newdp[j] = pres[j - minLength]
            dp = newdp
            pres = [0] * n  # 开始计算前缀和数组
            for j in range(minLength * (i + 1) - 1, n):
                pres[j] = pres[j - 1] + dp[j]
        return pres[-minLength] % (10**9 + 7)  # 最后一个切分肯定是以n-1结尾，通过上一个切分的前缀和可以得出


s = Solution()
assert s.beautifulPartitions("242538614532395749146912679859", 1, 6) == 1
assert s.beautifulPartitions(s="23542185131", k=3, minLength=3) == 1
assert s.beautifulPartitions(s="3312958", k=3, minLength=1) == 1
assert s.beautifulPartitions(s="23542185131", k=3, minLength=2) == 3

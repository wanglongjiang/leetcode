'''
2484. 统计回文子序列数目
困难
13
相关企业
给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。

提示：

如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
 

示例 1：

输入：s = "103301"
输出：2
解释：
总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
它们中有两个（都是 "10301"）是回文的。
示例 2：

输入：s = "0000000"
输出：21
解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
示例 3：

输入：s = "9999900000"
输出：2
解释：仅有的两个回文子序列是 "99999" 和 "00000" 。
 

提示：

1 <= s.length <= 104
s 只包含数字字符。
'''
'''
[TOC]

# 思路
前缀和

# 解题方法
首先，设二维前缀和数组prec[n][100]，prec[i][num]的意思是截止下标i，数字num的计数，数字num的取值范围为0..99。
遍历一次s，用prec统计所有数字的前缀和个数。

然后，用类似的方法计算后缀数组postc[n][100]

最后，遍历下标2..n-3，开始计算以s[i]为中心的回文串，因为2个数字的可能有100种，
所以可以遍历0..99的数字x，用prec[i-1]得到有多少个x，然后再从postc[i+1]得到i后面有多少个x的逆序数字。
2者的组合即为以s[i]为中心的回文串数


# 复杂度
- 时间复杂度: 
> $O(100n)$ 

- 空间复杂度: 
> $O(100n)$
'''


class Solution:
    def countPalindromes(self, s: str) -> int:
        n, MOD = len(s), 10**9 + 7
        if n < 5:
            return 0
        # 计算前缀2位数字
        prec = [None for _ in range(n)]
        prec[1] = [0] * 100
        prec[1][int(s[0:2])] += 1
        digitCount = [0] * 10
        digitCount[int(s[0])] += 1
        digitCount[int(s[1])] += 1
        for i in range(2, n):
            prec[i] = prec[i - 1].copy()
            num = int(s[i])
            for j in range(10):
                prec[i][j * 10 + num] += digitCount[j]
            digitCount[num] += 1
        # 计算后缀2位数字
        postc = [None for _ in range(n)]
        postc[-2] = [0] * 100
        postc[-2][int(s[-2:])] += 1
        digitCount = [0] * 10
        digitCount[int(s[-1])] += 1
        digitCount[int(s[-2])] += 1
        for i in range(n - 3, 0, -1):
            postc[i] = postc[i + 1].copy()
            num = int(s[i])
            for j in range(10):
                postc[i][num * 10 + j] += digitCount[j]
            digitCount[num] += 1
        # 计算数字num与逆序数字rnum的组合数
        ans = 0
        for i in range(2, n - 2):
            for num in range(100):
                t, o = divmod(num, 10)
                rnum = o * 10 + t
                ans = (ans + prec[i - 1][num] * postc[i + 1][rnum]) % MOD
        return ans


s = Solution()
assert s.countPalindromes("3")
assert s.countPalindromes("103301") == 2

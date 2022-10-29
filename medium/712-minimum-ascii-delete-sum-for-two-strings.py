'''
712. 两个字符串的最小ASCII删除和
给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
示例 2:

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
注意:

0 < s1.length, s2.length <= 1000。
所有字符串中的字符ASCII值在[97, 122]之间。
'''
'''
思路：动态规划
该题目为最长公共子序列(LCS)的变形，不同的是LCS对于每个字符的权重是1，这里是ascii值。
用动态规划，使2个字符串能够匹配的ascii值之和最大：
设dp[i+1][j+1]为s1[i]与s2[j]进行匹配时的公共子序列ascii值之和，故状态转移方程改为：
如果s1[i]==s2[j]，那么：dp[i + 1][j + 1] = max(dp[i][j] + ord(s1[i]), dp[i + 1][j], dp[i][j + 1])
如果s1[i]!=s2[j]，那么：dp[i + 1][j + 1] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1])

最终dp[m][n]为2个字符串的公共子序列ascii值最大和，
结果为s1的ascii值之和+s2的ascii值之和-2*dp[m][n]

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = max(dp[i][j] + ord(s1[i]), dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1])
        return sum(map(lambda char: ord(char), s1)) + sum(map(lambda char: ord(char), s2)) - 2 * dp[m][n]


s = Solution()
print(s.minimumDeleteSum("ccaccjp", "fwosarcwge") == 1399)
print(s.minimumDeleteSum(s1="sea", s2="eat"))
print(s.minimumDeleteSum(s1="delete", s2="leet"))

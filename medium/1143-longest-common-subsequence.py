'''
最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。
'''
'''
思路：动态规划。
设一个动态规划二维数组dp[m][n]
对比text1[i]、text2[j]，如果text1[i]=text2[j]，则dp[i][j]=dp[i-1][j-1]+1
如果text1[i]!=text2[j]，则dp[i][j]=max(dp[i-1][j], dp[i][j-1])
时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


s = Solution()
print(s.longestCommonSubsequence(text1="abcde", text2="ace"))
print(s.longestCommonSubsequence(text1="abc", text2="abc"))
print(s.longestCommonSubsequence(text1="abc", text2="def"))

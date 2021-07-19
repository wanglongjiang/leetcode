'''
最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

 

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。

 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母
'''
'''
思路：动态规划
设dp[i][j]为子字符串s[i..j]的最大子序列是回文串的长度，那么
> 当s[i]==s[j]时，dp[i][j] = max(dp[i + 1][j - 1] + 2, dp[i + 1][j], dp[i][j - 1])
> 当s[i]!=s[j]时，dp[i][j] = max(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1])

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        ans = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i + 1][j - 1] + 2, dp[i + 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1])
                ans = max(ans, dp[i][j])
        return ans


s = Solution()
print(s.longestPalindromeSubseq('a'))
print(s.longestPalindromeSubseq('cbbd'))
print(s.longestPalindromeSubseq('bbbab'))
print(s.longestPalindromeSubseq('bbbabbb'))
print(s.longestPalindromeSubseq('bbbdacbbb'))
print(s.longestPalindromeSubseq('bbbdacbdbdb'))
print(s.longestPalindromeSubseq('bbbdacbdbdbb'))

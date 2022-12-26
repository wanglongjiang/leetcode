'''
1312. 让字符串成为回文串的最少插入次数
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 s 成为回文串的 最少操作次数 。

「回文串」是正读和反读都相同的字符串。

 

示例 1：

输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
示例 2：

输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
示例 3：

输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
 

提示：

1 <= s.length <= 500
s 中所有字符都是小写字母。
'''
'''
思路：动态规划
题目可以转换成先求字符串最大回文子序列，找到最大回文子序列后，设最大回文子序列长度为l，剩余的字符都需要插入字符进行匹配，答案是n-l
求最大回文子序列长度，是一个经典的区间dp题目。
设dp[n][n]，dp[i][j]的意思是子串s[i..j]的最大回文子序列长度，
状态转移方程为：
当s[i]==s[j]，dp[i][j] = max(dp[i+1][j-1]+2,dp[i+1][j],dp[i][j-1]) 
当s[i]!=s[j]，dp[i][j] = max(dp[i+1][j-1],dp[i+1][j],dp[i][j-1])


时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1] + (2 if s[i] == s[j] else 0))
        return n - max(max(dp[i]) for i in range(n))


s = Solution()
print(s.minInsertions('zzazz'))

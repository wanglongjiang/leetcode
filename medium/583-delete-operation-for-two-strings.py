'''
583. 两个字符串的删除操作
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。



示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"


提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。
'''
'''
思路：动态规划
题目实际上是求最长公共子序列(LCS)，经典的dp题目。
设dp[i][j]是word1截止i，word2截止j，2个字符串的最长公共子序列长度，状态转移方程为：
如果word1[i]==word2[j]那么：dp[i][j] = 1+dp[i-1][j-1]
否则：dp[i][j] = max(dp[i][j-1],dp[i-1][j])

删除字符的次数是m+n-2*dp[m][n]

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if word1[i] == word2[j] else max(dp[i][j + 1], dp[i + 1][j])
        return m + n - 2 * dp[m][n]


s = Solution()
print(s.minDistance('a', 'a'))
print(s.minDistance('a1b2cdrerf', 'abcdefg'))

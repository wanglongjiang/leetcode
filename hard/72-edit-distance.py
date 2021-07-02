'''
编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
'''
'''
思路：动态规划
设二维动态规划数组dp[m][n]，
对于元素dp[i][j]的意思是截止word1的第i个字符和word2的第j字符，所用的最少编辑次数
有3种编辑方式：替换、删除、插入，根据3种编辑方式写出状态转移方程
如果word1[i]==word2[j]，dp[i][j] = dp[i-1][j-1]
否则：dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
在上面的min里面，3个最优子结构的意思是替换1个字符，删除1个字符，添加1个字符

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):  # 初始化边界初始值，j为0，如果要变换成word1，编辑次数就是字符串长度
            dp[i][0] = i
        for j in range(n + 1):  # 初始化边界初始值，i为0，如果要变换成word2，编辑次数就是字符串长度
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))

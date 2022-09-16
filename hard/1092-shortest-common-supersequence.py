'''
1092. 最短公共超序列
给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）

 

示例：

输入：str1 = "abac", str2 = "cab"
输出："cabac"
解释：
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。
 

提示：

1 <= str1.length, str2.length <= 1000
str1 和 str2 都由小写英文字母组成。
'''
'''
思路：动态规划
首先用动态规划求出2个字符串的最长公共子序列（LCS）矩阵
然后从m,n坐标出发，逆向回到左边界或上边界，移动的过程中输出超序列

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if str1[i] == str2[j] else max(dp[i + 1][j], dp[i][j + 1])
        ans = []
        i, j = m, n
        while i and j:
            if dp[i][j] == dp[i - 1][j]:  # 这种情况说明str1跳过了1个字符
                ans.append(str1[i - 1])
                i -= 1
            elif dp[i][j] == dp[i][j - 1]:  # 这种情况说明str2跳过了1个字符
                ans.append(str2[j - 1])
                j -= 1
            else:  # 这种情况说明str1[i]==str2[j]
                ans.append(str1[i - 1])
                i -= 1
                j -= 1
        if i:
            return str1[:i] + ''.join(ans[::-1])
        if j:
            return str2[:j] + ''.join(ans[::-1])
        return ''.join(ans[::-1])


s = Solution()
print(s.shortestCommonSupersequence(str1="a1b2c", str2="a4b5c"))
print(s.shortestCommonSupersequence(str1="abc", str2="abcd"))
print(s.shortestCommonSupersequence(str1="ab", str2="cd"))
print(s.shortestCommonSupersequence(str1="ab", str2="bc"))
print(s.shortestCommonSupersequence(str1="abac", str2="cab"))

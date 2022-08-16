'''
2370. 最长理想子序列
给你一个由小写字母组成的字符串 s ，和一个整数 k 。如果满足下述条件，则可以将字符串 t 视作是 理想字符串 ：

t 是字符串 s 的一个子序列。
t 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 k 。
返回 最长 理想字符串的长度。

字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。

注意：字母表顺序不会循环。例如，'a' 和 'z' 在字母表中位次的绝对差值是 25 ，而不是 1 。

 

示例 1：

输入：s = "acfgbd", k = 2
输出：4
解释：最长理想字符串是 "acbd" 。该字符串长度为 4 ，所以返回 4 。
注意 "acfgbd" 不是理想字符串，因为 'c' 和 'f' 的字母表位次差值为 3 。
示例 2：

输入：s = "abcd", k = 3
输出：4
解释：最长理想字符串是 "abcd" ，该字符串长度为 4 ，所以返回 4 。
 

提示：

1 <= s.length <= 105
0 <= k <= 25
s 由小写英文字母组成
'''
'''
思路：动态规划
遍历依次字符串s，设当前字符s[i]为char，
用动态规划思路：设dp[char]为截止字符char最长的理想字符串，状态转移方程为
dp[char] = max(dp[char-k]..dp[char+k])+1

时间复杂度：O(nk)
空间复杂度：O(1)
'''


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            charIdx = ord(char) - ord('a')
            dp[charIdx] = max(dp[i] for i in range(max(0, charIdx - k), min(26, charIdx + k + 1))) + 1
        return max(dp)


s = Solution()
print(s.longestIdealString("azaza", 25))
print(s.longestIdealString(s="acfgbd", k=2))

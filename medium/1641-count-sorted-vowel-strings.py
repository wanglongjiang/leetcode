'''
1641. 统计字典序元音字符串的数目
给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

 

示例 1：

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
示例 2：

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
示例 3：

输入：n = 33
输出：66045
 

提示：

1 <= n <= 50 
'''
'''
思路：动态规划
设二维动态规划数组dp[n+1][5]，
dp[i][j]的意思是长度为i的字符串，以元音字符j为结尾时有效字符串的个数。
dp[i][0]为1，意思是长度为i，以'a'结尾的字符串，只有1个。
dp[1][j]为1，意思是长度为1的字符串只有1个。
dp[i][j]=dp[i-1][0..j]，意思是长度为i的字符串，以元音j结尾的有效字符串，是长度为i-1比j小的元音结尾的有效字符串之和

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 5 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, 5):
                dp[i][j] = sum(dp[i - 1][:j + 1])
        return sum(dp[-1])


s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(2))

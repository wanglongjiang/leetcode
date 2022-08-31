'''
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。
'''
'''
思路：位运算 哈希
将元音出现的次数的奇偶用位来表示，当下标i,j出现位相同时，说明这2个下标之间形成的子串所有元音都是偶数个
遍历s，记录每个位置上的位，同时统计最长的串

时间复杂度：O(n)
空间复杂度：O(1)，5个元音最多有2^5种状态
'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels, count, bitmap = set('aeiou'), {0: -1}, 0
        ans = 0
        for i, c in enumerate(s):
            if c in vowels:
                bitmap ^= 1 << (ord(c) - ord('a'))
            if bitmap in count:
                ans = max(ans, i - count[bitmap])
            else:
                count[bitmap] = i
        return ans


s = Solution()
print(s.findTheLongestSubstring("eleetminicoworoep"))

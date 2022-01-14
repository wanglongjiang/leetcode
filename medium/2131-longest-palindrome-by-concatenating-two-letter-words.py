'''
2131. 连接两字母单词得到的最长回文串
给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。

请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。

请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。

回文串 指的是从前往后和从后往前读一样的字符串。

 

示例 1：

输入：words = ["lc","cl","gg"]
输出：6
解释：一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。
"clgglc" 是另一个可以得到的最长回文串。
示例 2：

输入：words = ["ab","ty","yt","lc","cl","ab"]
输出：8
解释：最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。
"lcyttycl" 是另一个可以得到的最长回文串。
示例 3：

输入：words = ["cc","ll","xx"]
输出：2
解释：最长回文串是 "cc" ，长度为 2 。
"ll" 是另一个可以得到的最长回文串。"xx" 也是。
 

提示：

1 <= words.length <= 10^5
words[i].length == 2
words[i] 仅包含小写英文字母。
'''

from typing import List
from collections import Counter
'''
思路：哈希
1. 遍历words，用哈希表进行计数
2. 遍历哈希表的key，如果其回文在哈希表中存在，将其计数分别减去min(key的计数，key的回文计数)。如果key为2个相同的字符，减去key的计数/2。结果+4
3. 再遍历一次哈希表，如果找到2个字符相同的key，且计数不为0，结果可以再加2

时间复杂度：O(n)
空间复杂度：O(1)，最多有26*26个单词
'''


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        ans = 0
        for key in counter.keys():
            if counter[key] > 0:
                if key[0] != key[1]:
                    pkey = key[1] + key[0]
                    if pkey in counter:
                        num = min(counter[key], counter[pkey])
                        counter[key] -= num
                        counter[pkey] -= num
                        ans += 4 * num
                else:
                    ans += (counter[key] // 2) * 4
                    counter[key] = counter[key] % 2
        for key in counter.keys():
            if counter[key] > 0 and key[0] == key[1]:
                ans += 2
                break
        return ans


s = Solution()
print(s.longestPalindrome(["em", "pe", "mp", "ee", "pp", "me", "ep", "em", "em", "me"]) == 14)
print(s.longestPalindrome(["lc", "cl", "gg"]) == 6)
print(s.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8)
print(s.longestPalindrome(["cc", "ll", "xx"]) == 2)

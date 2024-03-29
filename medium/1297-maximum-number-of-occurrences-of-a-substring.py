'''
1297. 子串的最大出现次数
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 

示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
 

提示：

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
'''

from operator import le
from typing import Counter
'''
思路：滑动窗口 哈希
设置一个大小为minSize的滑动窗口，当窗口内的不同字符数小于maxLetters时，将窗口内的子串保存到哈希表中计数
滑动窗口遍历完整个字符串后，哈希表中最大的即为答案
另外，maxSize是个无用的参数

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        wordCount, charCount = Counter(), Counter(s[:minSize])
        left, right, n = 0, minSize, len(s)
        if len(charCount) <= maxLetters:
            wordCount[s[left:right]] += 1
        while right < n:
            charCount[s[right]] += 1
            right += 1
            charCount[s[left]] -= 1
            if charCount[s[left]] == 0:
                del charCount[s[left]]
            left += 1
            if len(charCount) <= maxLetters:
                wordCount[s[left:right]] += 1
        return max(wordCount.values())


s = Solution()
print(s.maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))

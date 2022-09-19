'''
6181. 最长的字母序连续子字符串的长度
字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，
字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。

例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。

 

示例 1：

输入：s = "abacaba"
输出：2
解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
"ab" 是最长的字母序连续子字符串。
示例 2：

输入：s = "abcde"
输出：5
解释："abcde" 是最长的字母序连续子字符串。
 

提示：

1 <= s.length <= 105
s 由小写英文字母组成
'''
'''
思路：滑动窗口
设2个指针，分别指向滑动窗口的2端，当下一个字符是当前字符的后续，扩大右边界；否则滑动窗口重新从下一个字符开始设置。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left, right, ans, n = 0, 0, 1, len(s)
        while right + 1 < n:
            while right + 1 < n and (ord(s[right + 1]) - ord(s[right]) == 1):
                right += 1
            ans = max(ans, right - left + 1)
            left, right = right + 1, right + 1
        return ans


s = Solution()
print(s.longestContinuousSubstring('abcde'))
print(s.longestContinuousSubstring('abcdefghijklmnopqrstuvwxyz'))

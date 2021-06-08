'''
剑指 Offer 48. 最长不含重复字符的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

s.length <= 40000
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''
'''
思路：滑动窗口+哈希
设置2个指针构成滑动窗口，窗口内字符加入哈希表。
如果right指针向右移动扩大窗口的过程中出现重复字符，向右移动left指针，直至重复字符移出窗口

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left, right = 0, 0
        ans, n = 0, len(s)
        while right < n:
            while right < n and s[right] not in hashset:  # 扩大窗口范围，直至遇到重复字符
                hashset.add(s[right])
                right += 1
            ans = max(ans, len(hashset))
            while right < n and s[left] != s[right]:  # 缩小窗口范围，直至找到重复字符
                hashset.remove(s[left])
                left += 1
            if right < n:  # 将重复字符移出窗口
                left += 1
                right += 1
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(""))

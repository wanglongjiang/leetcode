'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
'''
思路：哈希 滑动窗口
设2个指针，形成滑动窗口，窗口内子串没有重复字符
当新的字符进入窗口会造成重复字符时，移动左边的指针，否则移动右边的指针

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxLen = 0
        strlen = len(s)
        end = -1
        map = set()
        for i in range(strlen):
            if i != 0:
                map.remove(s[i - 1])
            while end + 1 < strlen and s[end + 1] not in map:
                map.add(s[end + 1])
                end += 1
            maxLen = max(maxLen, end - i + 1)
        return maxLen


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb") == 3)
print(s.lengthOfLongestSubstring("bbbbb") == 1)
print(s.lengthOfLongestSubstring("pwwkew") == 3)
print(s.lengthOfLongestSubstring("") == 0)
print(s.lengthOfLongestSubstring("pwwkes") == 4)
print(s.lengthOfLongestSubstring("abba") == 2)

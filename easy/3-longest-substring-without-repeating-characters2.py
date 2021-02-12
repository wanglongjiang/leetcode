'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
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

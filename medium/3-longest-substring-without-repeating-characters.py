'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start = 0
        maxLen = 0
        end = 0
        for end in range(len(s)):
            findIdx = self.instr(s, start, end)
            if findIdx >= 0:
                maxLen = max(maxLen, end - start)
                start = findIdx + 1
        if end > start:
            maxLen = max(maxLen, end - start + 1)
        return maxLen

    def instr(self, s, start, end):
        for i in range(start, end):
            if s[i] == s[end]:
                return i
        else:
            return -1


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb") == 3)
print(s.lengthOfLongestSubstring("bbbbb") == 1)
print(s.lengthOfLongestSubstring("pwwkew") == 3)
print(s.lengthOfLongestSubstring("") == 0)
print(s.lengthOfLongestSubstring("pwwkes") == 4)

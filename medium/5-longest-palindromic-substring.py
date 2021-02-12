'''
给你一个字符串 s，找到 s 中最长的回文子串。
示例：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 回文有两种，一种是以当前字符为中心的奇数回文串，另外一种是以当前字符为左边的偶数回文
        # 如果有回文，下一个当前字符应该以回文最右边为基准开始
        index = 0
        maxLen = 0
        palinrome = ""
        strLen = len(s)
        while index < strLen:
            # 求偶数回文
            left, right = index, index + 1
            while left >= 0 and right < strLen:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    left += 1
                    right -= 1
                    break
            else:
                left += 1
                right -= 1
            evenLen = right - left + 1
            if evenLen > maxLen:
                maxLen = evenLen
                palinrome = s[left:right + 1]
            # 求奇数回文
            left, right = index - 1, index + 1
            while left >= 0 and right < strLen:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    left += 1
                    right -= 1
                    break
            else:
                left += 1
                right -= 1
            oddLen = right - left + 1
            if oddLen > maxLen:
                maxLen = oddLen
                palinrome = s[left:right + 1]
            index += 1
        return palinrome


s = Solution()
print(s.longestPalindrome("babad") == "bab")
print(s.longestPalindrome("cbbd") == "bb")
print(s.longestPalindrome("a") == "a")
print(s.longestPalindrome("ac") == "a")
print(s.longestPalindrome("aaaaa") == "aaaaa")

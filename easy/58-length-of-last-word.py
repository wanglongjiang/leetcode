'''
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        start = False
        for i in range(len(s) - 1, -1, -1):
            if not start and s[i] == ' ':
                pass
            elif not start:
                length += 1
                start = True
            elif s[i] != ' ':
                length += 1
            else:
                return length
        return length


s = Solution()
print(s.lengthOfLastWord("Hello World") == 5)
print(s.lengthOfLastWord(" ") == 0)

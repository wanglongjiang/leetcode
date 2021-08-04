'''
字符串中的单词数
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
'''


class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        n = len(s)
        i = 0
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i < n and s[i] != ' ':
                count += 1
                while i < n and s[i] != ' ':
                    i += 1
        return count

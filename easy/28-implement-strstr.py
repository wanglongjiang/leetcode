'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


s = Solution()
print(s.strStr("", "") == 0)
print(s.strStr("hello", "ll") == 2)
print(s.strStr("aaaaa", "aab") == -1)

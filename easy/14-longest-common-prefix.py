'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        while True:
            ch = ''
            for str in strs:
                if len(str) < index + 1 or (ch != '' and str[index] != ch):
                    return str[:index]
                elif ch == '':
                    ch = str[index]
            index += 1
        return strs[0][:index]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(s.longestCommonPrefix(["dog", "racecar", "car"]) == '')
print(s.longestCommonPrefix(["a", "a", "a"]) == 'a')
print(s.longestCommonPrefix(["", "", "a"]) == '')
print(s.longestCommonPrefix(["", "", ""]) == '')

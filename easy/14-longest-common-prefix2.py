'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        elif len(strs) == 1:
            return strs[0]
        commonPrefix = strs[0]
        for str in strs[1:]:
            if len(commonPrefix) > len(str):
                commonPrefix = commonPrefix[:len(str)]
            for i in range(len(commonPrefix)):
                if str[i] != commonPrefix[i]:
                    commonPrefix = commonPrefix[:i]
                    break
            if len(commonPrefix) == 0:
                return ""
        return commonPrefix


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(s.longestCommonPrefix(["dog", "racecar", "car"]) == '')
print(s.longestCommonPrefix(["a", "a", "a"]) == 'a')
print(s.longestCommonPrefix(["", "", "a"]) == '')
print(s.longestCommonPrefix(["", "", ""]) == '')

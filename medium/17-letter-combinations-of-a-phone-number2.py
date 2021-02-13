'''
电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
from typing import List
'''
解题思路：回溯法。
'''


class Solution:
    def __init__(self):
        super().__init__()
        self.mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        comms = []
        com = []

        def backtrack(index):
            if index == len(digits):
                return comms.append("".join(com))
            else:
                digit = digits[index]
                for char in self.mp[digit]:
                    com.append(char)
                    backtrack(index + 1)
                    com.pop()

        backtrack(0)
        return comms


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("235"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
print(s.letterCombinations("7"))

'''
电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
from typing import List
'''
解题思路：求所有字母的组合，每个数字代表的字母都要出现并与其他数字的代表的字母进行组合，
组合的总数为len(数字1映射的字母串)*len(数字2映射的字母串)*..len(数字n映射的字母串)
由于每个数字映射的字母不超过4个，且输入的数字长度不超过4，可以将组合数视为1个不定基数的整数，
该整数每3位表示一个数字代表的字母出现的索引。
通过一个大的迭代，将所有字母组合进行输出。
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
        maxIndexs = 0
        digitsLen = len(digits)
        for ch in digits:
            maxIndexs <<= 3
            maxIndexs |= len(self.mp[ch]) - 1
        comms = []
        indexs = 0
        while indexs <= maxIndexs:
            s = ''
            # 依次求出每个数字代表的字母，并拼接起来
            currentIndex = indexs
            for i in range(digitsLen - 1, -1, -1):
                digitCharIndex = currentIndex & 0x7
                currentIndex >>= 3
                s = self.mp[digits[i]][digitCharIndex] + s
            comms.append(s)
            # 求出下一个索引位置
            nextIndextsByLtoH = 0
            tmpMaxIndex = maxIndexs
            tmpNextIndex = indexs + 1
            for i in range(digitsLen - 1, -1, -1):
                maxDigitCharIndex = tmpMaxIndex & 0x7
                tmpMaxIndex >>= 3
                nextDigitCharIndex = tmpNextIndex & 0x7
                tmpNextIndex >>= 3
                if nextDigitCharIndex > maxDigitCharIndex:
                    nextIndextsByLtoH = (nextIndextsByLtoH << 3)
                    tmpNextIndex += 1
                else:
                    nextIndextsByLtoH = (
                        nextIndextsByLtoH << 3) | nextDigitCharIndex
            # 进位如果没有在上一个迭代中消化掉，说明有超过最大值的进位
            if tmpNextIndex > 0:
                return comms
            indexs = 0
            for i in range(digitsLen):
                indexs = (indexs << 3) | (nextIndextsByLtoH & 0x7)
                nextIndextsByLtoH >>= 3
        return comms


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("235"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
print(s.letterCombinations("7"))

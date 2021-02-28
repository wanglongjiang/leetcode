'''
有效数字
有效数字（按顺序）可以分成以下几个部分：

一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：

["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：

["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

'''
'''
思路：正则表达式
'''


class Solution:
    def __init__(self):
        super().__init__()
        import re
        # 整数部分
        intRe = r'((\+|-)?\d+)'
        # 小数部分
        decRe = r'((\+|-)?(\d+\.(\d+)?|\.\d+))'
        # 有效数字
        number = '^(' + intRe + '|' + decRe + ')(e' + intRe + ')?$'
        self.pattern = re.compile(number, re.I)

    def isNumber(self, s: str) -> bool:
        return self.pattern.match(s) is not None


s = Solution()
print(s.isNumber("0"))
print(s.isNumber("e"))
print(s.isNumber("."))
print(s.isNumber(".1"))
nums = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
ans = [0] * len(nums)
for i in range(len(nums)):
    ans[i] = s.isNumber(nums[i])
print(ans)
nums = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
ans = [0] * len(nums)
for i in range(len(nums)):
    ans[i] = s.isNumber(nums[i])
print(ans)

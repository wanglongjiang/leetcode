'''
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查第一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−2^31,  2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，
大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。
返回整数作为最终结果。
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        # skip space
        i = 0
        neg = False
        signs = False
        while i < len(s):
            if signs:
                if s[i].isnumeric:
                    break
                else:
                    return 0
            elif s[i] == ' ':
                i += 1
            elif s[i] == '+':
                i += 1
                signs = True
            elif s[i] == '-':
                neg = True
                i += 1
                signs = True
            elif s[i].isnumeric:
                break
            else:
                return 0
        maxInt = (2**31 - 1) // 10
        minInt = (2**31) // 10
        intNum = 0
        while i < len(s):
            if s[i].isnumeric():
                num = int(s[i])
                if not neg:
                    if intNum > maxInt or (intNum == maxInt and num > 7):
                        return 2**31 - 1
                else:
                    if intNum > minInt or (intNum == minInt and num > 8):
                        return -(2**31)
                intNum *= 10
                intNum += num
                i += 1
            else:
                break
        return intNum if not neg else -intNum


s = Solution()
print(s.myAtoi("42") == 42)
print(s.myAtoi("   -42") == -42)
print(s.myAtoi("4193 with words") == 4193)
print(s.myAtoi("words and 987") == 0)
print(s.myAtoi("-91283472332") == -2147483648)
print(s.myAtoi("91283472332") == 2**31 - 1)
print(s.myAtoi("2147483646") == 2147483646)

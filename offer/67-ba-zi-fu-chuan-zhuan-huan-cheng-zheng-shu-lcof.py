'''
把字符串转换成整数

写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，
请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
'''


class Solution:
    def strToInt(self, s: str) -> int:
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

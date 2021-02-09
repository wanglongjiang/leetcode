'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

特殊规则：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        product = 0
        while index < len(s):
            if s[index] == 'C':
                if index + 1 < len(s):
                    if s[index + 1] == 'M':
                        product += 900
                        index += 2
                        continue
                    elif s[index + 1] == 'D':
                        product += 400
                        index += 2
                        continue
                product += 100
            elif s[index] == 'X':
                if index + 1 < len(s):
                    if s[index + 1] == 'C':
                        product += 90
                        index += 2
                        continue
                    elif s[index + 1] == 'L':
                        product += 40
                        index += 2
                        continue
                product += 10
            elif s[index] == 'I':
                if index + 1 < len(s):
                    if s[index + 1] == 'X':
                        product += 9
                        index += 2
                        continue
                    elif s[index + 1] == 'V':
                        product += 4
                        index += 2
                        continue
                product += 1
            elif s[index] == 'M':
                product += 1000
            elif s[index] == 'D':
                product += 500
            elif s[index] == 'L':
                product += 50
            elif s[index] == 'V':
                product += 5
            index += 1
        return product


s = Solution()
print(s.romanToInt("III") == 3)
print(s.romanToInt("IV") == 4)
print(s.romanToInt("IX") == 9)
print(s.romanToInt("LVIII") == 58)
print(s.romanToInt("MCMXCIV") == 1994)

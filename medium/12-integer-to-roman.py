'''
整数转罗马数字

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

'''
'''
思路：贪心算法
将1，4，5，9...1000的所有罗马数字基础数字和特例放入栈中，然后用贪心算法，从大到小依次与待转化数值对比。
如果num>当前罗马数字，需要输出罗马数字，并将num减去当前罗马数字，剩余的值继续对比。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        mp = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        while len(mp) > 0:
            val, roman = mp.popitem()
            while num >= val:
                num -= val
                s += roman
        return s


s = Solution()
print(s.intToRoman(3) == 'III')
print(s.intToRoman(4) == "IV")
print(s.intToRoman(9) == 'IX')
print(s.intToRoman(58) == 'LVIII')
print(s.intToRoman(1994) == "MCMXCIV")

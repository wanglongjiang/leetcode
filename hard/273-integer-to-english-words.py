'''
273. 整数转换英文表示
将非负整数 num 转换为其对应的英文表示。



示例 1：

输入：num = 123
输出："One Hundred Twenty Three"
示例 2：

输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"
示例 3：

输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4：

输入：num = 1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


提示：

0 <= num <= 2^31 - 1
'''
'''
思路：逻辑判断
- 数字小于20，有直接对应的单词
- 在20和100之间，需要分解成十进制位和个位数
- 在99和1000之间，需要分解成百位和剩余部分
- 超过1000，需要分解成3个一组

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        nums19 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
            'Seventeen', 'Eighteen', 'Nineteen'
        ]
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def helper(num):
            if not num:
                return []
            if num < 20:
                return [nums19[num]]
            if num < 100:
                return [tens[num // 10]] + helper(num % 10)
            if num < 1000:
                return [nums19[num // 100]] + ['Hundred'] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000**(p + 1):
                    return helper(num // 1000**p) + [w] + helper(num % 1000**p)

        return ' '.join(helper(num))


s = Solution()
print(s.numberToWords(20))
print(s.numberToWords(123))
print(s.numberToWords(12345))
print(s.numberToWords(1234567))
print(s.numberToWords(1234567891))

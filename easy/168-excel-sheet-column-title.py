'''
Excel表列名称
给定一个正整数，返回它在 Excel 表中相对应的列名称。
'''
'''
思路，26进制数
'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while True:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            title = chr(ord('A') + remainder) + title
            if not columnNumber:
                break
        return title


s = Solution()
print(s.convertToTitle(701))
print(s.convertToTitle(1))
print(s.convertToTitle(27))
print(s.convertToTitle(28))
print(s.convertToTitle(2147483647))

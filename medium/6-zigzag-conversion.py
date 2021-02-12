'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
'''
"""
观察Z字符串序列可以看出，每个字符依次进入3行中每行的字符串，
可以设置3个辅助字符串进行接收，最后拼接3个字符串
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = 0
        gotoDown = True
        strs = [''] * numRows
        for c in s:
            strs[row] = strs[row] + c
            if gotoDown:
                row += 1
                if row == numRows - 1:
                    gotoDown = False
            else:
                row -= 1
                if row == 0:
                    gotoDown = True
        return "".join(strs)


s = Solution()
print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(s.convert("A", 1) == "A")
print(s.convert("AB", 1) == "AB")

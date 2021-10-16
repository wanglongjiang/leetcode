'''
393. UTF-8 编码验证
UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
对于 n 字节的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。

注意：
输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。

示例 1：

data = [197, 130, 1], 表示 8 位的序列: 11000101 10000010 00000001.

返回 true 。
这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
示例 2：

data = [235, 140, 4], 表示 8 位的序列: 11101011 10001100 00000100.

返回 false 。
前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。
'''
from typing import List
'''
思路：位运算
按照utf8编码，首先判断头部，然后根据头部是1..4字节，验证后续字节

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)
        while i < n:
            if 0x80 & data[i] == 0:  # 单字节
                i += 1
            elif 0xe0 & data[i] == 0xc0:  # 2字节
                i += 1
                if i < n and 0xc0 & data[i] == 0x80:
                    i += 1
                else:
                    return False
            elif 0xf0 & data[i] == 0xe0:  # 3字节
                i += 1
                if i < n - 1 and 0xc0 & data[i] == 0x80 and 0xc0 & data[i + 1] == 0x80:
                    i += 2
                else:
                    return False
            elif 0xf8 & data[i] == 0xf0:  # 4字节
                i += 1
                if i < n - 2 and 0xc0 & data[i] == 0x80 and 0xc0 & data[i + 1] == 0x80 and 0xc0 & data[i + 2] == 0x80:
                    i += 3
                else:
                    return False
            else:
                return False
        return True


s = Solution()
print(s.validUtf8([197, 130, 1]))
print(s.validUtf8([235, 140, 4]))

'''
解码方法
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，
或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6"和"06" 不同。

给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

'''
'''
解题思路：回溯

'''


class Solution:
    def __init__(self):
        super().__init__()
        self.decode = set()
        for i in range(1, 27):
            self.decode.add(str(i))

    def numDecodings(self, s: str) -> int:
        def decode(code):
            if code in self.decode:
                return 1
            return 0

        n = len(s)

        def backtrack(index: int):
            if index == n:
                return 1
            elif index == n - 1:
                return decode(s[index])
            else:
                one = decode(s[index])
                two = decode(s[index:index + 1])
                if one == 0 and two == 0:
                    return 0
                elif one == 1 and two == 1:
                    return backtrack(index + 1) + backtrack(index + 2)
                else:
                    return backtrack(index + 1)
                return backtrack(index + 1)

        return backtrack(0)


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("0"))
print(s.numDecodings("06"))
print(s.numDecodings("120"))
print(s.numDecodings("11"))
print(s.numDecodings("111"))
print(s.numDecodings("1111"))
print(s.numDecodings("11111"))

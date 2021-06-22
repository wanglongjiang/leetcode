'''
剑指 Offer 20. 表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格

小数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "    .1  "
输出：true
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
'''
'''
思路：状态机
根据数值的定义，写出状态机状态转移表，依次读入每个字符，查看是否能转移到下一个状态。最后结束输入，状态机能变成s_end状态

时间复杂度：O(n)，输入的字符串S只遍历一次
空间复杂度：O(1)
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        st_start, st_sign, st_int, st_dot, st_decimal, st_e, st_expsign, st_exp, st_endspace, st_end, st_open_dot = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ch_space, ch_num, ch_dot, ch_e, ch_sign, ch_end, ch_other = 0, 1, 2, 3, 4, 9, 99
        chMap = {' ': ch_space, '.': ch_dot, 'e': ch_e, 'E': ch_e, '-': ch_sign, '+': ch_sign}
        machine = {
            st_start: {  # 开始状态
                ch_space: st_start,
                ch_num: st_int,
                ch_dot: st_open_dot,
                ch_sign: st_sign
            },
            st_sign: {  # +-符号
                ch_dot: st_open_dot,
                ch_num: st_int
            },
            st_int: {  # 整数状态
                ch_num: st_int,
                ch_dot: st_dot,
                ch_e: st_e,
                ch_space: st_endspace,
                ch_end: st_end
            },
            st_open_dot: {  # 前面没有整数的小数点
                ch_num: st_decimal
            },
            st_dot: {  # 小数点
                ch_num: st_decimal,
                ch_e: st_e,
                ch_space: st_endspace,
                ch_end: st_end
            },
            st_decimal: {  # 小数部分状态
                ch_num: st_decimal,
                ch_e: st_e,
                ch_space: st_endspace,
                ch_end: st_end
            },
            st_e: {  # e
                ch_sign: st_expsign,
                ch_num: st_exp
            },
            st_expsign: {  # e的整数符号部分
                ch_num: st_exp
            },
            st_exp: {  # e的整数部分
                ch_num: st_exp,
                ch_space: st_endspace,
                ch_end: st_end
            },
            st_endspace: {  # 末尾空格部分
                ch_space: st_endspace,
                ch_end: st_end
            }
        }
        # 按照状态机进行状态遍历
        status = st_start
        for i in range(len(s)):
            ch = ch_other
            if s[i] in chMap:
                ch = chMap[s[i]]
            elif s[i].isdigit():
                ch = ch_num
            else:
                ch = ch_other
            if ch in machine[status]:
                status = machine[status][ch]  # 根据输入字符进行状态转移
            else:
                return False
        if ch_end in machine[status] and machine[status][ch_end] == st_end:
            return True
        return False


s = Solution()
print(not s.isNumber('.'))
print(s.isNumber("+100"))
print(s.isNumber("5e2"))
print(s.isNumber('-123'))
print(s.isNumber('3.1416'))
print(s.isNumber('-1E-16'))
print(s.isNumber('0123'))
print(s.isNumber('12e') is False)
print(s.isNumber('1a3.14') is False)
print(s.isNumber('1.2.3') is False)
print(s.isNumber('+-5') is False)
print(s.isNumber('12e+5.4') is False)

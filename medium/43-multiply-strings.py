'''
字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

num1 和 num2 的长度小于110。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''
'''
思路:模拟人计算乘积的方法，依次遍历乘数的每一位，依次乘被乘数的每一位，结果存储到1个数组里面
中间结果计算出来后再累加到累加数组（每次都左移1位）
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        len1 = len(num1)
        len2 = len(num2)
        sumarr = [0] * (len2 - 1)
        for i in range(len1):
            mularr = [0] * len2
            for j in range(len(num2)):
                mularr[j] = int(num1[i]) * int(num2[j])
            # 累积结果需要*10
            sumarr.append(0)
            for k in range(len2):
                sumarr[k + i] += mularr[k]
        # 进行进位操作
        carry = 0
        for i in range(len(sumarr) - 1, -1, -1):
            carry, sumarr[i] = divmod(sumarr[i] + carry, 10)
        if carry > 0:
            return str(carry) + ''.join(map(str, sumarr))
        else:
            return ''.join(map(str, sumarr))


s = Solution()
print(s.multiply("9", "99"))
print(s.multiply("123", "456"))
print(s.multiply("2", "3"))

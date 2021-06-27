'''
面试题 05.02. 二进制数转字符串
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。
如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

示例1:

 输入：0.625
 输出："0.101"
示例2:

 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示
提示：

32位包括输出中的"0."这两位。

'''
'''
思路：数学
不停的*2，直至小数部分为0

'''


class Solution:
    def printBin(self, num: float) -> str:
        ans = '0.'
        i = 0
        while num and i < 32:
            num *= 2
            i += 1
            if num >= 1:
                ans += '1'
                num -= 1
            else:
                ans += '0'
        return ans if not num else 'ERROR'


s = Solution()
print(s.printBin(0.625))
print(s.printBin(0.1))

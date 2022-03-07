'''
504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

 

示例 1:

输入: num = 100
输出: "202"
示例 2:

输入: num = -7
输出: "-10"
 

提示：

-107 <= num <= 107
'''
'''
思路：简单数学
建立7的指数表exp，然后在一个循环中，将num依次去除exp的每一级指数的整数倍

时间复杂度：O(logn)
空间复杂度：O(logn)
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = num < 0
        num = abs(num)
        exp = [1, 7]
        ans = []
        while exp[-1] <= num:
            exp.append(exp[-1] * 7)
        for i in range(len(exp) - 2, -1, -1):
            if num >= exp[i]:
                d, num = divmod(num, exp[i])
                ans.append(d)
            else:
                ans.append(0)
        ans = [str(i) for i in ans]
        return '-' + ''.join(ans) if neg else ''.join(ans)


s = Solution()
print(s.convertToBase7(1))
print(s.convertToBase7(100))
print(s.convertToBase7(-7))
print(s.convertToBase7(0))
print(s.convertToBase7(7))

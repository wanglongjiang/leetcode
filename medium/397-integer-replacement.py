'''
整数替换
给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？
'''
'''
思路：模拟计算
模拟题目中的要求计算
TODO 错误，需要修改
'''


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            count += 1
            if n & 1:  # 奇数
                n -= 1
            else:  # 偶数
                n >>= 1
        return count


s = Solution()
print(s.integerReplacement(8))
print(s.integerReplacement(7))
print(s.integerReplacement(4))

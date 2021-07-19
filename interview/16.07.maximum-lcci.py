'''
面试题 16.07. 最大数值
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。

示例：

输入： a = 1, b = 2
输出： 2
'''
'''
思路：位运算
计算出a与b的差c = a-b
然后用短路逻辑判断c&(1<<31)

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def maximum(self, a: int, b: int) -> int:
        c = a - b

        ans = b

        def assign():
            nonlocal ans
            ans = a

        c & (1 << 31) or assign()
        return ans


s = Solution()
print(s.maximum(a=1, b=2))

'''
面试题 16.01. 交换数字
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
'''

from typing import List
'''
思路：异或
3次异或可以交换2个变量，解释如下：
a=a^b
b=b^(a^b)=a
a=(a^b)^a=b
时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers


s = Solution()
print(s.swapNumbers([1, 2]))
print(s.swapNumbers([3, 9999]))

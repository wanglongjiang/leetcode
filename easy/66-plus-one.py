'''
加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

'''

from typing import List
'''
思路：从右向左迭代+进位
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if carry == 0:
                break
        if carry:
            digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([0]))
print(s.plusOne([9, 9, 9]))

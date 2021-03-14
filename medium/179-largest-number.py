'''
最大数
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
from typing import List
import math
'''
思路：转换输入为字符串数组，对字符串逆序排序（不同长度的，对比时用最后一位补成同样宽带），连结成字符串
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        K = int(math.ceil(math.log(max(nums), 10)))  # 整数的位数
        strs = [str(i) for i in nums]  # 转成字符串

        def sorter(item):
            return item.ljust(K, item[-1])  # 用最后1位补齐K位，例如55介于556、554之间，需要补成555

        strs.sort(key=sorter, reverse=True)
        return ''.join(strs)


s = Solution()
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([1]))
print(s.largestNumber([10]))

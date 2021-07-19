'''
最大数
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
from typing import List
'''
思路：排序
转换输入为字符串数组，对字符串逆序排序
排序对比不能简单对比字符串,需要连结起来对比
如果a+b>b+a则排序后a要在前面

与 剑指 Offer 42.[连续子数组的最大和](offer/42-lian-xu-zi-shu-zu-de-zui-da-he-lcof.py) 类似

时间复杂度:O(n^2),因为输入规模较小使用冒泡排序
空间复杂度:O(n)
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        strs = [str(i) for i in nums]  # 转成字符串
        # 冒泡排序
        for i in range(0, n - 1):
            for j in range(n - 1, i, -1):
                s1, s2 = strs[j] + strs[j - 1], strs[j - 1] + strs[j]
                if s1 > s2:
                    strs[j], strs[j - 1] = strs[j - 1], strs[j]
        ans = ''.join(strs)
        if len(ans) > 1 and ans[0] == '0':
            ans = '0'
        return ans


s = Solution()
print(s.largestNumber([55, 554]))
print(s.largestNumber([55, 556]))
print(s.largestNumber([34323, 3432]))
print(s.largestNumber([10, 2]))
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([1]))
print(s.largestNumber([10]))

'''
163. 缺失的区间
给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]
'''
from typing import List
'''
思路：数组一次遍历
遍历数组，2个相邻数字如果差>1，则需要插入一个缺失的区间

时间复杂度：O(n)
空间负责度：O(1)
'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        pre = lower
        nums.append(upper)
        for num in nums:
            if num - pre == 2:
                ans.append(str(num - 1))
            elif num - pre > 2:
                ans.append(str(pre + 1) + '->' + str(num - 1))
            pre = num
        return ans

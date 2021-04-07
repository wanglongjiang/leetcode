'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

提示：
0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''

from typing import List
'''
思路1，暴力搜索。
对于每个数字nums[i]，都向右搜索比它大的元素
时间复杂度：O(n^2)，结合输入的规模，达到10^10
空间复杂度：O(1)

思路2，线段树
TODO
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass

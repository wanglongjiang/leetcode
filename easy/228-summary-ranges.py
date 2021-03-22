'''
汇总区间
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，
并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
'''
from typing import List
'''
思路：一次遍历
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + '->' + str(nums[i - 1]))
                start = nums[i]
        if nums[-1] == start:
            ans.append(str(start))
        else:
            ans.append(str(start) + '->' + str(nums[-1]))
        return ans


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
print(s.summaryRanges([]))
print(s.summaryRanges([-1]))
print(s.summaryRanges([0]))

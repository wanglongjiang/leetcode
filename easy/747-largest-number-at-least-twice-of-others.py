'''
至少是其他数字两倍的最大数
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。

请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

 

示例 1：

输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 大于数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。
示例 2：

输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。
示例 3：

输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。
 

提示：

1 <= nums.length <= 50
0 <= nums[i] <= 100
nums 中的最大元素是唯一的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：一次遍历找到最大数和第二大的数
对比最大数和次大数，如果次大叔*2<=最大数，返回最大数的下标，否则返回-1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxIdx1, maxIdx2 = (0, 1) if nums[0] >= nums[1] else (1, 0)
        for i in range(2, len(nums)):
            if nums[i] > nums[maxIdx1]:
                maxIdx2 = maxIdx1
                maxIdx1 = i
            elif nums[i] > nums[maxIdx2]:
                maxIdx2 = i
        if nums[maxIdx2] * 2 <= nums[maxIdx1]:
            return maxIdx1
        return -1


s = Solution()
print(s.dominantIndex([1, 0]))

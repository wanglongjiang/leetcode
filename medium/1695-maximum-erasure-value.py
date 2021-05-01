'''
删除子数组的最大得分


给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
示例 2：

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
'''
from typing import List
'''
思路：双指针
设置2个指针left，right，和1个计数数组count[10^4]
如果count中没有重复数字，向右移动right指针，扩大子数组范围，将新的数字进行计数
如果count中有重复数字，向左移动left指针，直至重复数字消失
在移动right指针的过程中，记录最大子数组和maxSum
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        counter = [0] * 10001  # 计数器
        left, right = 0, 0
        dupNum = 0  # 重复数字
        maxSum, curSum = 0, 0
        while right < n:
            while right < n and dupNum == 0:  # 向右移动right指针，直至遇到重复元素
                if counter[nums[right]] == 0:
                    curSum += nums[right]
                    counter[nums[right]] += 1
                    right += 1
                else:
                    dupNum = nums[right]
                    counter[dupNum] += 1

            maxSum = max(maxSum, curSum)
            while left <= right and dupNum > 0:  # 向右移动left指针，直至重复元素消失
                if dupNum == nums[left]:
                    dupNum = 0
                    curSum += nums[right]
                    right += 1
                curSum -= nums[left]
                counter[nums[left]] -= 1
                left += 1
        return maxSum


s = Solution()
print(s.maximumUniqueSubarray([4, 2, 4, 5, 6]))
print(s.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))

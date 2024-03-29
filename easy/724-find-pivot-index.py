'''
寻找数组的中心下标
给你一个整数数组 nums ，请计算数组的 中心下标 。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

 

示例 1：

输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
示例 2：

输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
示例 3：

输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
 

提示：

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-pivot-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：前缀和
1. 计算数组的前缀和数组sums
2. 从左到右遍历数组
> 如果当前下标i的左侧和与右侧和相同，则返回true。即为：sums[i-1]=sums[n-1]-sums[i]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        if sums[n - 1] - nums[0] == 0:  # 判断以0作为中心下标
            return 0
        for i in range(1, n):
            if sums[i - 1] == sums[n - 1] - sums[i]:
                return i
        return -1


s = Solution()
print(s.pivotIndex([-1, -1, 0, 1, 1, 0]))
print(s.pivotIndex([-1, -1, 1, 1, 0, 0]))

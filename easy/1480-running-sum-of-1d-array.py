'''
1480. 一维数组的动态和
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。



示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
示例 3：

输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]


提示：

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''
from typing import List
'''
思路：求数组前缀和
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] + nums[i]
        return ans

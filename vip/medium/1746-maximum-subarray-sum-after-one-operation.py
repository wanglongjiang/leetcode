'''
1746. 经过一次操作后的最大子数组和
你有一个整数数组 nums。你只能将一个元素 nums[i] 替换为 nums[i] * nums[i]。

返回替换后的最大子数组和。

 

示例 1：

输入：nums = [2,-1,-4,-3]
输出：17
解释：你可以把-4替换为16(-4*(-4))，使nums = [2,-1,16,-3]. 现在，最大子数组和为 2 + -1 + 16 = 17.
示例 2：

输入：nums = [1,-1,1,1,-1,-1,1]
输出：4
解释：你可以把第一个-1替换为1，使 nums = [1,1,1,1,-1,-1,1]. 现在，最大子数组和为 1 + 1 + 1 + 1 = 4.
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''
from typing import List
'''
思路：TODO
'''


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        pass

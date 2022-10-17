'''
2439. 最小化数组中的最大值
给你一个下标从 0 开始的数组 nums ，它含有 n 个非负整数。

每一步操作中，你需要：

选择一个满足 1 <= i < n 的整数 i ，且 nums[i] > 0 。
将 nums[i] 减 1 。
将 nums[i - 1] 加 1 。
你可以对数组执行 任意 次上述操作，请你返回可以得到的 nums 数组中 最大值 最小 为多少。

 

示例 1：

输入：nums = [3,7,1,6]
输出：5
解释：
一串最优操作是：
1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。
2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。
3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。
nums 中最大值为 5 。无法得到比 5 更小的最大值。
所以我们返回 5 。
示例 2：

输入：nums = [10,1]
输出：10
解释：
最优解是不改动 nums ，10 是最大值，所以返回 10 。
 

提示：

n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109
'''
from math import ceil
from typing import List
'''
思路：贪心
从题意中可以看出，数组右边的元素可以减小自己，添加给左边任意的元素。
遇到一个较大的值时，最佳策略就是使其与左边的元素和平均分配。
遍历一次nums，遍历过程中求和sum，然后sum/(i+1)即为最小最大值

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans, sum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans, ceil(sum / (i + 1)))
        return ans

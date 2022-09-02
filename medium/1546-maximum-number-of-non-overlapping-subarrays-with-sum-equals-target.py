'''
1546. 和为目标值且不重叠的非空子数组的最大数目
给你一个数组 nums 和一个整数 target 。

请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
示例 2：

输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2
解释：总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
示例 3：

输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3
示例 4：

输入：nums = [0,0,0], target = 0
输出：3
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
'''

from typing import List
'''
思路：前缀和 哈希
计算nums的前缀和数组prefixsum，可以看出，对于prefixsum[i]，
如果前面有一个下标j，满足prefixsum[i]-target=prefixsum[j]，那么子数组j+1..i的和为target。
为快速查找j，需要将每个位置上的前缀和保存到哈希表中。
另外，需要一个辅助数组count，count[i]保存以i为结尾的子数组，前面的所有不相交子数组的个数

时间复杂度：O(n)
空间复杂度；O(n)
'''


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefixsumMap, count = {nums[0]: 0}, [0] * n
        premax = [0] * n
        count[0] = 1 if nums[0] == target else 0
        premax[0] = 1 if nums[0] == target else 0
        presum = nums[0]
        for i in range(1, n):
            presum += nums[i]
            if presum == target:
                count[i] = max(count[i], 1)
            if presum - target in prefixsumMap:
                count[i] = max(count[i], premax[prefixsumMap[presum - target]] + 1)
            premax[i] = max(count[i], premax[i - 1])
            prefixsumMap[presum] = i
        return max(count)


s = Solution()
print(s.maxNonOverlapping([1, 3, -3, 0, 2, 3, -2, -2], 4))
print(s.maxNonOverlapping([0, 0, 0], 0))
print(s.maxNonOverlapping([-1, -2, 8, -3, 8, -5, 5, -4, 5, 4, 1], 5))
print(s.maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))
print(s.maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))
print(s.maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))
print(s.maxNonOverlapping(nums=[0, 0, 0], target=0))

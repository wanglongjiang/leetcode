'''
1099. 小于 K 的两数之和
给你一个整数数组 nums 和整数 k ，返回最大和 sum ，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum < k 。
如果没有满足此等式的 i,j 存在，则返回 -1 。



示例 1：

输入：nums = [34,23,1,24,75,33,54,8], k = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：nums = [10,20,30], k = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。


提示：

1 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= 2000
'''
from typing import List
'''
思路：排序 双指针
首先对数组进行排序
然后2个指针初始指向数组的两端，
如果nums[left]+nums[right]>=k，则需要向左移动right指针
如果不满足上述条件，需要向右移动left指针，同时记录当前和sum

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = -1
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                if (s := nums[left] + nums[right]) > ans:
                    ans = s
                left += 1
        return ans


s = Solution()
print(s.twoSumLessThanK(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60))
print(s.twoSumLessThanK(nums=[10, 20, 30], k=15))

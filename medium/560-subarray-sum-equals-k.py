'''
和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''
from typing import List
'''
思路：滑动窗口
left，right构成滑动窗口，
    如果窗口内的和<k，向右移动right指针
    如果窗口内的和>k，向右移动left指针
    如果窗口内的和==k，计数+1，向右移动right指针,left指针
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 1
        total = nums[0]
        count = 0
        while left < n:
            if total > k:
                total -= nums[left]
                left += 1
                continue
            if total == k:
                total -= nums[left]
                left += 1
                count += 1
            if right < n:
                total += nums[right]
                right += 1
            if right == n and total < k:
                break
        return count


s = Solution()
print(s.subarraySum(nums=[1, 1, 1], k=2))

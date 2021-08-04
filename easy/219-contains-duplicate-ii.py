'''
存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
'''
from typing import List
'''
思路，滑动窗口 哈希
设left,right指针构成滑动窗口，滑动窗口最大为k，即right-left<k。
滑动窗口内的元素加入哈希表hashset，如果在移动滑动窗口的过程中，hashset中出现重复元素，返回true

时间复杂度：O(n)
空间复杂度：O(k)
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right, n = 0, 0, len(nums)
        hashset = set()
        while right < n:
            if len(hashset) < k:
                if nums[right] in hashset:
                    return True
                hashset.add(nums[right])
                right += 1
            else:
                hashset.remove(nums[left])
                left -= 1
        return False

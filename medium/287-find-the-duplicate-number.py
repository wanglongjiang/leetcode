'''
寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
'''
from typing import List
'''
思路：二分查找。取mid=n//2 ，查找其中==mid的数字个数为eqNum，>mid的数字个数为gtNum，<mid的数字个数为ltNum。
    如果eqNum >1 则mid为重复数
    如果gtNum>n-mid，则重复数在>mid的区间中，需要在这个区间折半查找。
    如果ltNum>mid-1，则重复数在<mid的区间中，需要在这个区间折半查找。
    由于每次查找都折半，最多经过logN次查找会找到这个数
    时间复杂度：O(nlogn)
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, hight = 0, len(nums) - 1
        while True:
            mid = (low + hight) >> 1
            eq, gt, lt = 0, 0, 0
            for i in nums:
                if i == mid:
                    eq += 1
                elif hight >= i > mid:
                    gt += 1
                elif mid > i >= low:
                    lt += 1
            if eq > 1:  # 重复数为mid
                return mid
            elif gt > hight - mid:  # 重复数在>mid的区间中，修改边界条件查找
                low = mid + 1
            else:  # 重复数在<mid的区间中，修改边界条件查找
                hight = mid - 1


s = Solution()
print(s.findDuplicate([4, 3, 1, 4, 2]))
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
print(s.findDuplicate([1, 1]))
print(s.findDuplicate([1, 1, 2]))

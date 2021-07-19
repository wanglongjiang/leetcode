'''
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
'''
from typing import List
'''
思路：哈希表判断是否有重复的元素
时间复杂度：O(n)
空间复杂度：O(n)

思路2：索引追踪 空间复杂度O(1)
以数组中的值为索引，将该位置设置为-1，如果发现了待设置的位置上已经为-1，则为重复值。
也即：设a=nums[i]，那么找到nums[a]，如果nums[a]=-1，则a是重复元素，如果nums[a]!=-1，则将nums[a]设置为-1，再查找原nums[a]的值，按前面的方式尝试设置为-1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路1，哈希
    def findRepeatNumber1(self, nums: List[int]) -> int:
        all = set()
        for num in nums:
            if num in all:
                return num
            else:
                all.add(num)

    # 思路2，索引追踪
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = nums[i]
            if a == i:
                nums[i] = -1
            elif a == -1:
                continue
            else:
                while True:
                    b = nums[a]
                    if b == -1:
                        return a
                    else:
                        nums[a] = -1
                    a = b

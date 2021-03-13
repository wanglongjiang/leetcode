'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''
from typing import List
'''
思路1，用hash保存元素，第2次出行时删除。未想到使用O(1)空间的线性时间复杂度的算法。
思路2，持续异或。利用a^b^a=b的异或特性，唯一的数会遗留下来。
    空间复杂度：O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for i in range(1, len(nums)):
            n ^= nums[i]
        return n

    def singleNumber1(self, nums: List[int]) -> int:
        numSet = set()
        for i in nums:
            if i in numSet:
                numSet.remove(i)
            else:
                numSet.add(i)
        return numSet.pop()


s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 1, 2, 1, 2]))

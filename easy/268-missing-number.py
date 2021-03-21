'''
丢失的数字
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
'''
from typing import List
'''
思路：异或。把整个数组与1-n的整数进行异或。由于相同数字异或后变成0，最后剩下的数字就是缺少的。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= (i + 1) ^ nums[i]
        return ans


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([0]))

'''
缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

 

进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

'''

from typing import List
'''
思路：因数组长度<=300，可以设置一个长度为10的整数数组，每位代表大小为n的数字是否出现过
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mask = [0] * 10
        min, max = 1, len(nums)
        for num in nums:
            if num >= min and num <= max:
                bitIndex = (num - 1) % 30
                mask[(num - 1) // 30] |= 0x1 << bitIndex
        for i in range(len(mask)):
            for j in range(30):
                if mask[i] & 0x1 == 0:
                    return i * 30 + j + 1
                mask[i] >>= 1
        return 0


s = Solution()
print(
    s.firstMissingPositive([
        99, 94, 96, 11, 92, 5, 91, 89, 57, 85, 66, 63, 84, 81, 79, 61, 74, 78,
        77, 30, 64, 13, 58, 18, 70, 69, 51, 12, 32, 34, 9, 43, 39, 8, 1, 38,
        49, 27, 21, 45, 47, 44, 53, 52, 48, 19, 50, 59, 3, 40, 31, 82, 23, 56,
        37, 41, 16, 28, 22, 33, 65, 42, 54, 20, 29, 25, 10, 26, 4, 60, 67, 83,
        62, 71, 24, 35, 72, 55, 75, 0, 2, 46, 15, 80, 6, 36, 14, 73, 76, 86,
        88, 7, 17, 87, 68, 90, 95, 93, 97, 98
    ]))
print(
    s.firstMissingPositive([
        39, 8, 43, 12, 38, 11, -9, 12, 34, 20, 44, 32, 10, 22, 38, 9, 45, 26,
        -4, 2, 1, 3, 3, 20, 38, 17, 20, 25, 41, 35, 37, 18, 37, 34, 24, 29, 39,
        9, 36, 28, 23, 18, -2, 28, 34, 30
    ]))
print(s.firstMissingPositive([1, 1]))
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
print(s.firstMissingPositive([7, 8, 9, 11, 12, 1, 2, 3]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, -1]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, -1]))

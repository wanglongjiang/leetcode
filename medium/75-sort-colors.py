'''
颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
'''
from typing import List
'''
思路：计数排序
使用计数排序对仅有3个数字的数组进行排序
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        j = 0
        for i in range(len(nums)):
            if count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1


s = Solution()
a = [2, 0, 2, 1, 1, 0]
s.sortColors(a)
print(a)
a = [2, 0, 1]
s.sortColors(a)
print(a)
a = [1]
s.sortColors(a)
print(a)
a = [0]
s.sortColors(a)
print(a)

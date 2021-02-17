'''
下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
'''
from typing import List
'''
思路：寻找下一个序列的实质是：可以将序列看成左边为高位，右边为低位的数字，可以从右往左寻找第1个变小的数字a，
将数字a提升,提升需要从a的左边降序数组里面查找仅大于a的数字b，将b与a交换，再将b左边的降序数组逆序
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def search(start, end, target):
            for i in range(end - 1, start - 1, -1):
                if nums[i] > target:
                    return i

        def reverse(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                newIndex = search(i, len(nums), nums[i - 1])
                nums[i - 1], nums[newIndex] = nums[newIndex], nums[i - 1]
                reverse(i)
                return
        nums.reverse()


s = Solution()
a = [1, 2, 3]
s.nextPermutation(a)
print(a)
a = [3, 2, 1]
s.nextPermutation(a)
print(a)
a = [1, 1, 5]
s.nextPermutation(a)
print(a)
a = [1]
s.nextPermutation(a)
print(a)
a = [1, 3, 2]
s.nextPermutation(a)
print(a)

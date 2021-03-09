'''
删除排序数组中的重复项 II
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
from typing import List
'''
思路：与26题类似
有2个指针，第1个指针指向当前元素，第2个指针指向删重后的数组末尾（第2个指针可以通过1个被删除的元素数来计算得到）
与26题不同的是，还需要维护1个计数器，记录重复元素出现的次数
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num = None
        numCount = 0
        deleted = 0
        for i in range(len(nums)):
            if num == nums[i]:
                if numCount == 2:
                    deleted += 1
                else:
                    numCount += 1
                    nums[i - deleted] = num
            else:
                num = nums[i]
                numCount = 1
                nums[i - deleted] = num
        return len(nums) - deleted


s = Solution()
a = [1, 1, 1, 2, 2, 3]
print(s.removeDuplicates(a))
print(a)
a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(s.removeDuplicates(a))
print(a)
a = [0, 1, 2, 3]
print(s.removeDuplicates(a))
print(a)
a = [3]
print(s.removeDuplicates(a))
print(a)
a = [-1, -1, -1, -2, -2, -2, 1, 2, 3]
print(s.removeDuplicates(a))
print(a)

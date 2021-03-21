'''
只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''
from typing import List
'''
思路：快排算法里面的分区。
随机从nums中选取pivot,利用快速排序算法里面的分区函数，分成2个区，<pivot的 和 >=pivot的。如果其中一个分区大小不是3的整数倍，
    说明目标元素出现在那个分区。需要继续对分区进行再分区。重复分区过程，直至有分区大小==1，则返回该分区的数。
时间复杂度：O(n)，快排的时间复杂度为O(nlogn)，这里因为每次只对一半的分区进行再分区，所以时间复杂度为O(n)
空间复杂度：O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import random

        def partition(start, end):
            if end - start == 1:
                return nums[start]
            k = random.randint(start, end - 1)
            nums[start], nums[k] = nums[k], nums[start]
            pivot = nums[start]
            i, j = start, end - 1
            while i < j:  # 分成2个区
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            lowSize = i - start  # 小于pivot的分区大小
            if lowSize and lowSize % 3:  # 唯一数在小的分区
                return partition(start, i)
            highSize = end - i  # 大于pivot的分区大小
            if highSize and highSize % 3:  # 唯一数在大的分区
                return partition(i, end)

        return partition(0, len(nums))


s = Solution()
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(s.singleNumber([2, 2, 3, 2]))

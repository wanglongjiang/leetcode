'''
只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

 

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
'''
from typing import List
'''
思路：快排算法里面的分区。
随机从nums中选取pivot,利用快速排序算法里面的分区函数，分成2个区，<pivot的 和 >=pivot的。
    如果2个分区的大小是奇数，说明2个唯一数分别出现在2个分区里，对2个分区分别求所有元素的异或，剩下的元素就就是唯一数，
    如果2个分区的大小是偶数，对其中一个分区求所有元素的异或，如果结果为0，说明唯一数在另外一个分区，需要对含有唯一数的分区继续分区。
    重复以上过程，如果有1个分区大小为2，异或结果不为0，这2个数都是唯一数。
时间复杂度：O(n)，快排的时间复杂度为O(nlogn)，这里因为每次只对一半的分区进行再分区，所以时间复杂度为O(n)
空间复杂度：O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        import random

        def partition(start, end):
            if (end - start) == 2:
                ans.append(nums[start])
                ans.append(nums[start + 1])
                return
            # 分成大小2个区
            i = random.randint(start, end - 1)
            nums[start], nums[i] = nums[i], nums[start]
            pivot = nums[start]
            i, j = start, end - 1
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            # 对分区进行检查，如果大小都是奇数，2个唯一数分布在2个区里面
            if (i - start) & 1:
                num1 = nums[start]
                for k in range(start + 1, i):
                    num1 ^= nums[k]
                ans.append(num1)
                num2 = nums[i]
                for k in range(i + 1, end):
                    num2 ^= nums[k]
                ans.append(num2)
                return
            else:  # 分区大小为偶数，通过异或确定唯一数在哪个分区
                if i - start > 0:
                    num = nums[start]
                    for k in range(start + 1, i):
                        num ^= nums[k]
                    if num:  # 异或结果不为0，说明唯一数在这个分区
                        partition(start, i)
                        return
                partition(i, end)  # 前面分区大小为0，或者前面分区的异或结果为0，说明唯一数在后面的分区

        partition(0, len(nums))
        return ans


s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))
print(s.singleNumber([-1, 0]))
print(s.singleNumber([0, 1]))

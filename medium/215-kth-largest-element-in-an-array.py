'''
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''
from typing import List
'''
思路，快排分区。利用快速排序里面的分区函数，对输入数组进行分区，然后查看2个分区的大小，
    如果K落在小的分区，继续查找第K大的数
    如果K落在大的分区，需要将K减去小的分区的大小
    如果K==1，分区大小也为1，则返回该数
时间复杂度：O(n)，快排的时间复杂度为O(nlogn)，这里因为每次只对一半的分区进行再分区，所以时间复杂度为O(n)
空间复杂度：O(1)
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(k, start, end):
            if end - start == 1:  # 分区大小只有1，直接返回
                return nums[start]
            # 下面按照快排的分区方法对数组分成大小2个区
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
            lowSize = i - start
            if k == lowSize + 1:  # k正好与分区切割点相同，返回该数字
                return pivot
            if k <= lowSize:  # k落在小的分区，继续查找
                return partition(k, start, i)
            else:  # k落在大的分区，在大数的分区第k大的数变成k-lowSize-1大的数
                return partition(k - lowSize - 1, i + 1, end)

        return partition(k, 0, len(nums))


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

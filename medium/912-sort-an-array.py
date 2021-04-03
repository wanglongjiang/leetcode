'''
排序数组
给你一个整数数组 nums，请你将该数组升序排列。

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''
from typing import List
'''
思路：快排+计数排序
计数排序需要遍历2次数组，时间复杂度为：10^5
快排时间复杂度为O(nlogn)，如果数组大小达到10^4，也能达到10^5。
数组如果小于10^4，采用快排，否则使用计数排序
快排:时间复杂度O(nlogn)，空间复杂度O(logn)
计数排序：时间复杂度O(n)，空间复杂度O(n)
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 定义快速排序函数
        import random

        def qsort(start, end):
            if end - start == 1:
                return
            i = random.randint(start, end - 1)
            if start != i:
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
            if i - start > 1:
                qsort(start, i)
            if end - i > 2:
                qsort(i + 1, end)

        # 计数排序
        def csort():
            arr = [0] * 100001
            for num in nums:
                arr[num + 50000] += 1
            c = 0
            for i in range(100001):
                while arr[i] > 0:
                    arr[i] -= 1
                    nums[c] = i - 50000
                    c += 1
                    if c == n:
                        return

        if n < 10000:
            qsort(0, n)
        else:
            csort()
        return nums


s = Solution()
print(s.sortArray([5, 2, 3, 1]))
print(s.sortArray([5, 1, 1, 2, 0, 0]))

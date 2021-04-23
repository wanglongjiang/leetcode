'''
面试题 10.11. 峰与谷
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。
例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
提示：

nums.length <= 10000
'''
from typing import List
'''
思路：排序后交替插入
1、数组排序
2、设置2个指针，left,right分别指向排序后数组的左边、中间，然后交替复制回原数组
时间复杂度：O(nlogn)
空间复杂度：O(n)
TODO
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        num2 = sorted(nums)
        n = len(nums)
        mid = n // 2 + n & 1
        left, right = 0, mid + 1
        i = 0
        while left <= mid:
            nums[i] = num2[left]
            if right < n:
                nums[i + 1] = num2[right]
            left += 1
            right += 1
            i += 2

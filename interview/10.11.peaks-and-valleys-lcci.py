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
1、数组从大到小排序
2、将后半部分复制到辅助数组
3、将前半部分复制到偶数下标
4、将辅助数组中的元素复制到奇数下标

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        n = len(nums)
        temp = nums[n // 2 + n % 2:]
        for i in range(n - len(temp) - 1, 0, -1):
            nums[2 * i] = nums[i]
        for i in range(len(temp)):
            nums[2 * i + 1] = temp[i]
        return nums


s = Solution()
print(s.wiggleSort([5, 3, 1, 2, 3]))
print(s.wiggleSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(s.wiggleSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''
交换一次的先前排列
给你一个正整数的数组 A（其中的元素不一定完全不同），请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、
按字典序排列小于 A 的最大可能排列。

如果无法这么操作，就请返回原数组。

提示：

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^4
'''
from typing import List
'''
思路：双指针
从左向右单调递增的数组使最小的排列，无法交换
如果不是最小排列，肯定有arr[i-1]>arr[i]存在，此时交换arr[i],arr[i-1]就比原排列小
但这种情况下不一定是小于原排列的最大排列。需要从arr[i]..arr[n-1]之间寻找仅仅小于arr[i-1]的元素，相同元素选择靠近arr[i-1]的
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # 从右向左寻找第1个arr[i]>arr[i-1]
        left = -1
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                left = i - 1
                break
        if left < 0:  # 数组为递增排列，无法交换，直接返回原数组
            return arr
        # 从右向左寻找仅小于arr[left]的元素
        right = n - 1
        while arr[right] >= arr[left]:  # 跳过大于等于pivot的元素
            right -= 1
        # 跳过相同的元素
        while right > left and arr[right] == arr[right - 1]:
            right -= 1
        arr[right], arr[left] = arr[left], arr[right]
        return arr


s = Solution()
print(s.prevPermOpt1([1]))
print(s.prevPermOpt1([1, 2]))
print(s.prevPermOpt1([2, 1]))
print(s.prevPermOpt1([2, 1, 1]))
print(s.prevPermOpt1([3, 2, 1]))
print(s.prevPermOpt1([1, 1, 5]))
print(s.prevPermOpt1([1, 9, 4, 6, 7]))
print(s.prevPermOpt1([3, 1, 1, 3]))

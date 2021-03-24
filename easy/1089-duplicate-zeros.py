'''
复写零
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
'''
from typing import List
'''
思路：2次遍历。第1次统计0的个数m，第2次从n-m处开始向末尾复制数字。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        m = 0
        externd = 0
        for i in range(n):
            if m + i == n:
                externd = 0
                break
            elif m + i > n:  # 添加0之后数值长度越界
                externd = 1
                break
            if arr[i] == 0:
                m += 1
        left, right = n - m - 1, n - 1
        if externd:  # 数组越界，需要特殊处理
            arr[right] = 0
            right -= 1
        while left < right:
            arr[right] = arr[left]
            right -= 1
            if arr[left] == 0:  # 遇到0重复复制1次
                arr[right] = 0
                right -= 1
            left -= 1


s = Solution()
arr = [0, 7]
s.duplicateZeros(arr)
print(arr)
arr = [8, 4, 5, 0, 0, 0, 0, 7]
s.duplicateZeros(arr)
print(arr)
arr = [1, 0, 2, 3, 0, 4, 5, 0]
s.duplicateZeros(arr)
print(arr)

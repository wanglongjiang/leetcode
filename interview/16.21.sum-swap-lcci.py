'''
面试题 16.21. 交换和
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。

返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。

示例:

输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
示例:

输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
提示：

1 <= array1.length, array2.length <= 100000
'''
from typing import List
'''
思路：哈希
先求2个数组的差diff = sum(arr1)-sum(arr2)
那么如果想要达到相等，diff的绝对值必须为偶数，且从arr1中提取的数据arr[i]-diff/2在arr2中存在。
检查arr[i]-diff/2在arr2中存在，可以使用哈希表，将arr2全部加入哈希表

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1) - sum(array2)
        if abs(diff) % 2:
            return []
        diff //= 2
        arr2 = set(array2)
        for num in array1:
            if num - diff in arr2:
                return [num, num - diff]
        return []

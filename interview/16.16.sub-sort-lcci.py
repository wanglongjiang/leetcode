'''
面试题 16.16. 部分排序
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。
注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，
若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

示例：

输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
提示：

0 <= len(array) <= 1000000
'''
from typing import List
import bisect
'''
思路：双指针+二分查找
left指针从左到右遍历数组，如果有arr[i]>arr[i+1]则停止，在遍历过程中记录最大值maxVal
right指针从右到左遍历数组，如果有arr[i]<arr[i-1]则停止，在遍历过程中记录最小值minVal
再遍历arr[left..right]，更新maxVal和minVal
在arr[0..left]找到minVal应该插入的位置：start
在arr[right..n]找到maxVal应该插入的位置：end
[start,end]就是结果

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        left, right = 0, n - 1
        minVal, maxVal = float('inf'), float('-inf')
        # 定位开始变乱序的left下标
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                maxVal = array[i]
                left = i
                break
        if maxVal == float('-inf'):  # 如果数组一直是单调递增，则返回[-1,-1]
            return [-1, -1]
        # 定位开始变乱序的right下标
        for i in range(n - 1, 0, -1):
            if array[i] < array[i - 1]:
                minVal = array[i]
                right = i
                break
        # 找到乱序中最大值最小值
        for i in range(left, right + 1):
            if array[i] > maxVal:
                maxVal = array[i]
            elif array[i] < minVal:
                minVal = array[i]
        # 乱序中的最小值应该插入到0..left内，最大值应该插入到left..n内，使用二分查找
        left = bisect.bisect_right(array, minVal, 0, left)
        right = bisect.bisect_left(array, maxVal, right, n)
        return [left, right - 1]


s = Solution()
print(s.subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
print(s.subSort([1, 3, 9, 7, 5]))

'''
山脉数组的峰顶索引

符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

 

示例 1：

输入：arr = [0,1,0]
输出：1
示例 2：

输入：arr = [0,2,1,0]
输出：1
示例 3：

输入：arr = [0,10,5,2]
输出：1
示例 4：

输入：arr = [3,4,5,1]
输出：2
示例 5：

输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
 

提示：

3 <= arr.length <= 10^4
0 <= arr[i] <= 10^6
题目数据保证 arr 是一个山脉数组
 

进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？
'''
from typing import List
'''
思路：二分查找
对于1个山脉数组，取数组中间的元素mid=(start+end)/2，
> 如果mid-1到mid是升序，则mid..end里有峰顶
> 如果mid-1到mid是降序，则start..mid-1里有峰顶
重复执行上面过程，直至数组大小<=3
对于长度<=3的数组，峰顶为max(arr[start],arr[start+1],arr[end])

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while end - start >= 3:
            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid]:
                start = mid
            else:
                end = mid - 1
        return start if arr[start] > arr[start + 1] else (end if arr[end] > arr[start + 1] else start + 1)


s = Solution()
print(s.peakIndexInMountainArray([0, 1, 0]))
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
print(s.peakIndexInMountainArray([0, 10, 5, 2]))
print(s.peakIndexInMountainArray([3, 4, 5, 1]))
print(s.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))

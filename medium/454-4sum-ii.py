'''
四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，
最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
from typing import List
import bisect
'''
思路：二分查找
问题实际上是求A,B,C,D四个数组每个拿出1个元素的所有组合和为0的数量，如果采用暴力组合，时间复杂度是O(n^4)也就是500^4,会超时
可以分别求A,B的组合之和，C,D的组合之和，然后对其中一个排序，再遍历另外一个，二分查找排序过的数组中是否有符合条件的数。

时间复杂度：O(n^2logn^2)
空间复杂度：O(n^2)
'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        arr1, arr2 = [], []
        for i in range(n):
            for j in range(n):
                arr1.append(nums1[i] + nums2[j])
                arr2.append(nums3[i] + nums4[j])
        arr2.sort()
        arr2.append(float('inf'))  # 添加1个哨兵
        ans = 0
        for num in arr1:
            leftIdx = bisect.bisect_left(arr2, -num)
            if arr2[leftIdx] == -num:  # 如果要满足4个数之和为0，因为num为A+B之和，故需要二分查找0-num
                rightIdx = bisect.bisect_right(arr2, -num)
                ans += rightIdx - leftIdx  # 因为arr2中可能有多个组合满足要求，需要全部累计上
        return ans


s = Solution()
print(s.fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))

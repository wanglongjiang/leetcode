'''
1574. 删除最短的子数组使剩余数组有序
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

示例 1：

输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
示例 2：

输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
示例 3：

输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
示例 4：

输入：arr = [1]
输出：0
 

提示：

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
'''

from typing import List
import bisect
'''
思路：二分查找
先从左到右搜索非递减子数组，然后从右向左搜索非递减子数组，整个数组被切分成立了left,mid,right3个部分。
因为只删除1个子数组，所以答案是mid要被删除，然后再加上mid两边的若干个元素，直至剩余的部分都是非递减的。
搜索mid两边的元素数，需要
1、遍历left的每个元素，在right中搜索大于等于它的，记录此时的中间数组的大小
2、遍历right的每个元素，在left中搜索小于它的，记录此时的两端的子数组大小；


时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # 先找到3个数组的分界点left,right
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:  # 整个数组都是非递减，直接返回0
            return 0
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        # 遍历left数组，查找满足要求的right数组的下标，2者直接即为需要删除的子数组，用ans保留其大小
        ans = n
        for i in range(left + 1):
            j = bisect.bisect_left(arr, arr[i], right)
            ans = min(ans, j - i - 1)
        # 遍历right数组，查找满足要求的left数组的下标，2者直接即为需要删除的子数组，用ans保留其大小
        for i in range(right, n):
            j = bisect.bisect_left(arr, arr[i], 0, left + 1)
            ans = min(ans, i - j)
        return ans


s = Solution()
print(s.findLengthOfShortestSubarray([16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15]))
print(s.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
print(s.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))
print(s.findLengthOfShortestSubarray([1, 2, 3]))
print(s.findLengthOfShortestSubarray([1]))

'''
1508. 子数组和排序后的区间和
给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数字的数组。

请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

 

示例 1：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
输出：13 
解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。
示例 2：

输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6
解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 3 + 3 = 6 。
示例 3：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50
 

提示：

1 <= nums.length <= 10^3
nums.length == n
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2
'''

from email.errors import HeaderParseError
from typing import List
import heapq
'''
思路：优先队列（堆）
设一个最大堆maxHeap和一个最小堆minHeap，分别保存最小和最大的left-1个数、n * (n + 1) / 2-right个数
1、用2层的循环生成所有子数组的和subArrSum，累加到所有子数组和allArrSum，再将subArrSum分别尝试加入最大堆和最小堆
2、上述1计算完成后，用allArrSum减掉最大堆和最小堆中的数值

时间复杂度：O(n^2logn^2)
空间复杂度：O(n^2)
'''


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        allArrSum = 0
        maxHeap, minHeap = [], []
        lowSize, highSize = left - 1, n * (n + 1) / 2 - right
        for i in range(n):
            subArrSum = 0
            for j in range(i, n):
                subArrSum += nums[j]
                allArrSum += subArrSum
                if highSize == 0:
                    pass
                elif len(minHeap) == highSize:
                    if minHeap[0] < subArrSum:
                        heapq.heapreplace(minHeap, subArrSum)
                else:
                    heapq.heappush(minHeap, subArrSum)
                if lowSize == 0:
                    pass
                elif len(maxHeap) == lowSize:
                    if maxHeap[0] < -subArrSum:
                        heapq.heapreplace(maxHeap, -subArrSum)
                else:
                    heapq.heappush(maxHeap, -subArrSum)
        return (allArrSum + sum(maxHeap) - sum(minHeap)) % (10**9 + 7)


s = Solution()
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=3, right=4))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
print(s.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=10))

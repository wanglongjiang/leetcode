'''
659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。

如果可以完成上述分割，则返回 true ；否则，返回 false 。



示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
示例 3：

输入: [1,2,3,4,4,5]
输出: False


提示：

1 <= nums.length <= 10000
'''
from typing import List
import heapq
'''
思路：贪心 堆
设一个最小堆，用于保存序列的最后一个元素和序列长度构成的元组。
遍历数组，对比最小堆第0个元素，
如果是最后一个元素的后继，将最小堆元素出堆，将(当前元素，长度+1)压入堆
如果不是最后一个元素的后续，检查其长度，如果长度<3则不满足题意，否则将最小元素出堆

上面的算法通过使用堆，每次都将元素附加到最短的序列上。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        h = [(nums[0], 1)]
        for i in range(1, len(nums)):
            if nums[i] == h[0][0] + 1:
                prev, length = heapq.heappop(h)
                heapq.heappush(h, (nums[i], length + 1))
            elif nums[i] == h[0][0]:
                heapq.heappush(h, (nums[i], 1))
            else:
                while h and h[0][0] + 1 < nums[i]:
                    prev, length = heapq.heappop(h)
                    if length < 3:
                        return False
                if h:
                    heapq.heappush(h, (nums[i], heapq.heappop(h)[1] + 1))
                else:
                    heapq.heappush(h, (nums[i], 1))
        while h and h[0][1] >= 3:
            heapq.heappop(h)
        return not h


s = Solution()
print(s.isPossible([1, 2, 3, 3, 4, 5]))
print(s.isPossible([1, 2, 3, 4, 4, 5]))
print(s.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))

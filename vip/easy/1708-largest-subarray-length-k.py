'''
1708. 长度为 K 的最大子数组
在数组 A 和数组 B 中，对于第一个满足 A[i] != B[i] 的索引 i ，当 A[i] > B[i] 时，数组 A 大于数组 B。

例如，对于索引从 0 开始的数组：

[1,3,2,4] > [1,2,2,4] ，因为在索引 1 上， 3 > 2。
[1,4,4,4] < [2,1,1,1] ，因为在索引 0 上， 1 < 2。
一个数组的子数组是原数组上的一个连续子序列。

给定一个包含不同整数的整数类型数组 nums ，返回 nums 中长度为 k 的最大子数组。



示例 1:

输入: nums = [1,4,5,2,3], k = 3
输出: [5,2,3]
解释: 长度为 3 的子数组有： [1,4,5]、 [4,5,2] 和 [5,2,3]。
在这些数组中， [5,2,3] 是最大的。
Example 2:

输入: nums = [1,4,5,2,3], k = 4
输出: [4,5,2,3]
解释: 长度为 4 的子数组有： [1,4,5,2] 和 [4,5,2,3]。
在这些数组中， [4,5,2,3] 是最大的。
示例 3:

输入: nums = [1,4,5,2,3], k = 1
输出: [5]


提示：

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^9
nums 中的所有整数都是不同的。


进阶：如果允许 nums 中存在相同元素，你该如何解决该问题？
'''
from typing import List
'''
思路：分治
整个数组可以划分成n-k+1个子数组，可以用分治，归并的方法比较出最大的子数组
1. 分治，将子数组划分成2部分，如果每一部分的大小大于1，需要进一步划分，直至只含有1个子数组，将该子数组的开始索引返回。
2. 归并，对比2个子数组，返回较大的子数组开始索引

时间复杂度：O(klogn)
空间复杂度：O(logn)
'''


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        def dc(start, end):
            if end > start:
                mid = (start + end) // 2
                a1 = dc(start, mid)  # 分成2部分，分别求其最大数组
                a2 = dc(mid + 1, end)
                for i in range(k):  # 对比子数组中最大的2个并返回
                    if nums[a1 + i] > nums[a2 + i]:
                        return a1
                    elif nums[a1 + i] < nums[a2 + i]:
                        return a2
                return a1  # 两个子子数组完全一样，任意返回一个
            else:
                return start

        i = dc(0, len(nums) - k)
        return nums[i:i + k]


s = Solution()
print(s.largestSubarray(nums=[1, 4, 5, 2, 3], k=3))
print(s.largestSubarray(nums=[1, 4, 5, 2, 3], k=4))
print(s.largestSubarray(nums=[1, 4, 5, 2, 3], k=1))

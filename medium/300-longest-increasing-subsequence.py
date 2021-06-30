'''
最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
提示：

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''
from typing import List
import bisect
'''
思路：二分查找
设一个dp数组，其为有序数组，用于保存最长子序列。
遍历nums每个元素，将其尝试加入dp数组：
> 如果nums[i]大于dp数组中所有元素，说明最长子序列可以变长，需要扩大dp大小。
> 如果nums[i]不大于dp中所有元素，需要定位其在有序数组dp中应该所处的位置，替换原先的元素。
这么做的目的是在保持最长子序列长度不变的情况下，减小以往保存的元素大小，以便新的元素加入时，能够出现上面的情况：大于dp中所有元素，可以扩展最长子序列

类似题目：
- 673.[最长递增子序列的个数](medium/673-number-of-longest-increasing-subsequence.py)
- 面试题 17.08.[马戏团人塔](interview/17.08.circus-tower-lcci.py)

时间复杂度：O(nlogn)，需要遍历nums每个元素，在遍历的时候需要查找nums[i]在dp中的索引，所以是n*logn
空间复杂度：O(n)
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)


s = Solution()
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))

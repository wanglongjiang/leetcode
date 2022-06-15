'''
719. 找出第 k 小的距离对
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0 
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
提示:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''

from typing import List
import bisect
'''
思路：排序 二分查找
与之相似的：
- 668.[乘法表中第k小的数](hard/668-kth-smallest-number-in-multiplication-table.py)

设第k个距离对的距离是x，二分查找x，计算数组距离对是否多于k

时间复杂度：O(nlognlogn)
空间复杂度：O(1)
'''


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def getSmallCount(x):  # 计算比x小的距离对个数
            ans = 0
            for i in range(1, len(nums)):
                ans += i - bisect.bisect_left(nums, nums[i] - x, 0, i)  # 查找距离对小于x的索引，并累计满足要求的个数
            return ans

        l, r, ans = 0, nums[-1] - nums[0], 0
        while l <= r:
            mid = (l + r) // 2
            if getSmallCount(mid) >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


s = Solution()
print(s.smallestDistancePair([62, 100, 4], 2))
print(s.smallestDistancePair([1, 3, 1], 1))
print(s.smallestDistancePair(nums=[1, 1, 1], k=2))
print(s.smallestDistancePair([1, 6, 1], 3))

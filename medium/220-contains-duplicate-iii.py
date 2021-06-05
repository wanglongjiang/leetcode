'''
存在重复元素 III
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 10^4
0 <= t <= 231 - 1
'''
from typing import List
'''
思路1，暴力搜索
设置3个指针，left,mid,right，初始指向第0，第1个元素，第k个元素，
left，right指向窗口的2端，窗口依次向右移动，窗口移动的过程中，执行下面的过程：
把mid指针从left至right移动，在移动的过程中判断是否符合abs(nums[i] - nums[right]) <= t

时间复杂度：O(n*k)，left,right指针移动n次，mid指针在窗口内移动k次
空间复杂度：O(1)

思路2，treemap，见java版的代码
思路3，桶排序
'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        left, right = 0, 1
        while left < right:
            while right < n and right - left <= k:  # 确保在窗口内进行判断
                for mid in range(left, right):  # 从left..right-1的元素都与nums[right]进行对比，判断是否符合条件
                    if abs(nums[mid] - nums[right]) <= t:
                        return True
                right += 1  # 移动right指针，扩大窗口
            left += 1
            if right == n:  # right越界，需要回退到合法的位置
                right = n - 1
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1, 2, 2, 3, 4, 5], 3, 0))
print(s.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
print(s.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))
print(s.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))

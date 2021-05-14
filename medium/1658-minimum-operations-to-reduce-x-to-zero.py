'''
将 x 减到 0 的最小操作数
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 

示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
示例 2：

输入：nums = [5,6,7,8,9], x = 4
输出：-1
示例 3：

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
'''
from typing import List
'''
思路：滑动窗口
使数组左部和右部构成的滑动窗口内数值之和<=x。
初始滑动窗口完全在数组左部，然后逐步缩小左部窗口，扩大右部窗口，在窗口移动的过程中记录窗口最小的大小。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, right, n = 0, len(nums), len(nums)
        total = 0
        # 先扩大左侧窗口大小，直至和>=x
        while total < x and left < n:
            total += nums[left]
            left += 1
        ans = float('inf')
        if total < x:
            return -1
        if total == x:
            ans = left
        # 移动滑动窗口（缩小左侧，扩大右侧）
        while left >= 0 or right >= 0:
            while total > x and left > 0:  # 缩小左侧窗口
                left -= 1
                total -= nums[left]
            if total == x:
                ans = min(ans, left + n - right)
                if left > 0:
                    left -= 1
                    total -= nums[left]
            while total < x and right > 0:  # 扩大右侧窗口
                right -= 1
                total += nums[right]
            if total == x:
                ans = min(ans, left + n - right)
                if right > 0:
                    right -= 1
                    total += nums[right]
            if left == 0 and total >= x:
                break
        if ans > n:
            return -1
        return ans


s = Solution()
print(
    s.minOperations([
        5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996, 8902, 228, 4461, 90, 7321, 7893, 4879, 9987,
        1146, 8177, 1073, 7254, 5088, 402, 4266, 6443, 3084, 1403, 5357, 2565, 3470, 3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530,
        9630, 1521, 2174, 5027, 4833, 3483, 445, 8300, 3194, 8784, 279, 3097, 1491, 9864, 4992, 6164, 2043, 5364, 9192, 9649, 9944, 7230, 7224, 585, 3722, 5628,
        4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968, 9983, 3540, 9224, 6216, 9665, 8070, 31, 3555, 4198, 2626, 9553, 9724, 4503,
        1951, 9980, 3975, 6025, 8928, 2952, 911, 3674, 6620, 3745, 6548, 4985, 5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639
    ], 565610))
print(s.minOperations(nums=[1, 1, 4, 2, 3], x=5))
print(s.minOperations(nums=[5, 6, 7, 8, 9], x=4))
print(s.minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))

'''
统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''
from typing import List
'''
思路：滑动窗口
按照套路，left,right构成滑动窗口，
1. 先移动right指针扩大窗口，直至子数组内奇数个数为k
2. 记录当前left指针为lleft，尝试移动left指针，将子数组左部的偶数移出窗口，但不要将奇数移出
3. 记录将当前right指针赋值给rright，然后尝试移动rright指针，尝试将子数组右边的偶数移入窗口，但不要将奇数移入
4. lleft和rright包含了left，right构成的区间，（abs(lleft-left)+1）*(abs(right-rright)+1)即为此次窗口构成的子数组数量
5. 将left=left+1，移出一个奇数；right = rright，right指针移动到右边界后，回到上面的1.继续下一轮查找

复杂度分析：
> 时间复杂度：O(n)，4个指针最多每个指针遍历一次数组
> 空间复杂度：O(1)
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        odd = 0
        ans = 0
        while right < n:
            while right < n:  # 扩大窗口，直至子数组内奇数个数为k
                if nums[right] % 2:
                    odd += 1
                    if odd == k:
                        break
                right += 1
            if right == n and odd < k:  # 无法再凑够k个奇数，退出循环
                break
            lleft = left
            while left <= right and nums[left] % 2 == 0:  # 移出左部的偶数，找到满足k个奇数的最小窗口
                left += 1
            rright = right + 1
            while rright < n and nums[rright] % 2 == 0:  # 移动rright指针，直至遇到下一个奇数
                rright += 1
            rright -= 1
            ans += ((left - lleft) + 1) * ((rright - right) + 1)  # 累计子数组个数
            left = left + 1  # 将最左侧奇数移出窗口，进入下一次迭代
            odd -= 1
            right = rright + 1
        return ans


s = Solution()
print(s.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(s.numberOfSubarrays(nums=[2, 4, 6], k=1))
print(s.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))

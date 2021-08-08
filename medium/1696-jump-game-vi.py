'''
跳跃游戏 VI
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，
你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。

你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。

请你返回你能得到的 最大得分 。

提示：

 1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4
'''

from typing import List
'''
思路：动态规划
动态规划状态转移方程为：
maxsum[i]=nums[i]+max(maxsum[i-1]...maxsum[i-k])
该动态规划时间复杂度为O(nk)，因为n、k最坏情况下是10^5，故有可能达到10^10，超时了。
进一步思考，如果nums[i]为正整数，经过i的和一定大于上一个经过的坐标j，
故如果遇到正整数，上面的状态转移方程可以改为max(maxsum[i-1]...maxsum[max(最近的正整数坐标,i-k)])
如果输入数组中均匀分布有一定数量的正整数，时间复杂度会改进不少，但最坏情况下（全部是负数）仍然是O(nk)
TODO
'''


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxsum = [0] * n
        maxsum[0] = nums[0]
        i = 1
        while i < n:
            while i < n and nums[i] >= 0:  # 对于非负数，全部要经过该元素
                maxsum[i] = nums[i] + maxsum[i - 1]
                i += 1
            if i == n:
                break
            # 向右寻找下一个非负数
            right = i + 1
            while right < n and nums[right] < 0:
                right += 1
            if right == n:  # 确保最后经过的元素是最后1个
                right = n - 1
            if right - i + 1 <= k:  # 如果区间宽度小于等于k，直接跳过该负数区间
                maxsum[right] = nums[right] + maxsum[i]
            else:  # 区间宽度大于k，需要用状态转移方程计算最大和
                maxsum[i] = nums[i] + maxsum[i - 1]
                for j in range(i + 1, right + 1):
                    leftMax = maxsum[j - 1]
                    for l in range(j - 1, max(i - 2, j - k - 1), -1):  # 向左最多搜索k个值，搜索和最大的
                        leftMax = max(leftMax, maxsum[l])
                    maxsum[j] = nums[j] + leftMax
            i = right + 1
        return maxsum[-1]


s = Solution()
print(s.maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))  # 7
print(s.maxResult(nums=[10, -5, -2, 4, 0, 3], k=3))  # 17
print(s.maxResult(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2))  # 0

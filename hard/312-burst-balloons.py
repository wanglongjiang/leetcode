'''
戳气球
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。


提示：

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
'''
from typing import List
'''
思路1，暴力回溯
暴力回溯算法，每层回溯都尝试从数组中挑选1个戳破
时间复杂度：O(n!)
空间复杂度：O(n)


'''


class Solution:
    # 思路1，暴力回溯
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def backtrack(arr):
            if len(arr) == 2:
                return max(arr[0] + arr[0] * arr[1], arr[0] * arr[1] + arr[1])
            maxCoins = 0
            for i in range(len(arr)):
                if i == 0:
                    coins = arr[i] * arr[i + 1] + backtrack(arr[1:])
                elif i == len(arr) - 1:
                    coins = arr[i] * arr[i - 1] + backtrack(arr[:len(arr) - 1])
                else:
                    coins = arr[i - 1] * arr[i] * arr[i + 1] + backtrack(arr[:i] + arr[i + 1:])
                maxCoins = max(maxCoins, coins)
            return maxCoins

        return backtrack(nums)


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
print(s.maxCoins([1, 5]))

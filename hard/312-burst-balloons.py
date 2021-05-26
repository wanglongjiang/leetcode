'''
戳气球
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：

输入：nums = [1,5]
输出：10


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

思路2，动态规划
设动态规划数组dp[m][n]，意思是区间nums[m...n]能戳破气球能获得的最大硬币数
要想获得区间内能获得的最大硬币数，需要有一个变量k指向最后戳破的气球，k在区间[m..n]之间
状态转移方程为：dp[m][n] = max(dp[m][k]+dp[k][n]+nums[m]*nums[k]*nums[n])，k需要遍历从m到n的位置

时间复杂度：O(n^3)
空间复杂度：O(n^2)
'''


class Solution:
    # 思路1，暴力回溯
    def maxCoins1(self, nums: List[int]) -> int:
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

    # 思路2，动态规划
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1]  # 为简化计算原nums头尾各添加一个元素1
        coins.extend(nums)
        coins.append(1)
        n = len(coins)
        dp = [[0] * n for _ in range(n)]
        for i in range(2, n):  # 区间大小为i
            for j in range(n - i):  # 区间范围由2重循环确定，为[j..j+i]，区间在0..n-i之间滑动
                for k in range(j + 1, j + i):  # 最后戳破的气球k，需要遍历区间内每一种可能
                    dp[j][j + i] = max(dp[j][j + i], dp[j][k] + dp[k][j + i] + coins[j] * coins[k] * coins[j + i])
        return dp[0][n - 1]


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
print(s.maxCoins([1, 5]))

'''
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''
from typing import List
'''
思路：动态规划。
该题目具有最优子结构，可以写出动态规划转换公式，对于第i个房屋，能偷到的最大金额为隔1个屋或隔2个屋再加上第i个屋的钱
f(i)=max(f(i-2)+h[i], f(i-3)+h[i])，对于i>=3
f(0)=0
f(1)=1
f(2)=f(0)+h[i]
根据上面的公式可以写出动态规划算法。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        if n == 0:
            return 0
        if n >= 1:
            f[0] = nums[0]
            if n == 1:
                return f[0]
        if n >= 2:
            f[1] = nums[1]
        if n >= 3:
            f[2] = f[0] + nums[2]
        for i in range(3, n):
            f[i] = max(f[i - 2] + nums[i], f[i - 3] + nums[i])  # 如果偷第i个屋的钱，最多能偷到隔1个屋或隔2个屋再加本屋的钱
        return max(f[-1], f[-2])


s = Solution()
print(s.rob([1, 2, 3, 1]) == 4)
print(s.rob([2, 7, 9, 3, 1]) == 12)
print(s.rob([1]))
print(s.rob([]))
print(s.rob([1, 2]))

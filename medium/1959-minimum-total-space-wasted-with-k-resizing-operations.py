'''
1959. K 次调整数组大小浪费的最小总空间
你正在设计一个动态数组。给你一个下标从 0 开始的整数数组 nums ，其中 nums[i] 是 i 时刻数组中的元素数目。
除此以外，你还有一个整数 k ，表示你可以 调整 数组大小的 最多 次数（每次都可以调整成 任意 大小）。

t 时刻数组的大小 sizet 必须大于等于 nums[t] ，因为数组需要有足够的空间容纳所有元素。t 时刻 浪费的空间 为 sizet - nums[t] ，
总 浪费空间为满足 0 <= t < nums.length 的每一个时刻 t 浪费的空间 之和 。

在调整数组大小不超过 k 次的前提下，请你返回 最小总浪费空间 。

注意：数组最开始时可以为 任意大小 ，且 不计入 调整大小的操作次数。

 

示例 1：

输入：nums = [10,20], k = 0
输出：10
解释：size = [20,20].
我们可以让数组初始大小为 20 。
总浪费空间为 (20 - 10) + (20 - 20) = 10 。
示例 2：

输入：nums = [10,20,30], k = 1
输出：10
解释：size = [20,20,30].
我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。
总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。
示例 3：

输入：nums = [10,20,15,30,20], k = 2
输出：15
解释：size = [10,20,20,30,30].
我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。
总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 106
0 <= k <= nums.length - 1
'''
from typing import List
'''
​ 我们可以将数组分成k + 1段，每段的权值是长度 * 最大值 - 该段总和，最后要每段的权值加和最小。

​ 首先，通过预处理，将每段的权值计算出来。

​ 之后，让dp(i, j)记录前i个数字分成j段时的最小权值和。

​ 则有dp(i, j) = min(dp(0 ~ i - 1, j - 1))，即第i个数字分成j段只能从前i个数字里的j - 1段中转移过来。

'''


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 预处理数组 g
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            # 记录子数组的最大值
            best = float("-inf")
            # 记录子数组的和
            total = 0
            for j in range(i, n):
                best = max(best, nums[j])
                total += nums[j]
                g[i][j] = best * (j - i + 1) - total

        f = [[float("inf")] * (k + 2) for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 2):
                for i0 in range(i + 1):
                    f[i][j] = min(f[i][j], (0 if i0 == 0 else f[i0 - 1][j - 1]) + g[i0][i])

        return f[n - 1][k + 1]

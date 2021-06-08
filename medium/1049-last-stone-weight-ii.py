'''
最后一块石头的重量 II

有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。


示例 1：
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

示例 2：
输入：stones = [31,26,33,21,40]
输出：5

示例 3：
输入：stones = [1,2]
输出：1


提示：

1 <= stones.length <= 30
1 <= stones[i] <= 100
'''
from typing import List
'''
思路：01背包问题，动态规划
将数组分为2个子数组，2个子数组的石头互相碰撞，最后剩下的石头重量最少。也就是2个数组的和之差最少。
求2个数组的和之差最少，可以转化为01背包问题：
设allWeight为所有石头的重量，取出数组中若干石头，如果能恰好取出一半的重量也就是allWeight/2，和之差为0，最理想，
用01背包思路，问题变成了求取出数组中若干石头，使其尽量接近allWeight/2。
设背包容量half=allWeight/2，找到最接近half的重量w，那么allWeight-2*w即为2个子数组的差，也就是最小重量。

时间复杂度：O(n*v)，v为allWeight/2
空间复杂度：O(v)
'''


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        allWeight = sum(stones)
        half = allWeight // 2
        dp = [False] * (half + 1)
        dp[0] = True
        # 下面是01背包套路算法
        for w in stones:
            for v in range(half, w - 1, -1):
                if dp[v - w]:
                    dp[v] = True
        # 找到最接近half的重量
        for v in range(half, -1, -1):
            if dp[v]:
                return allWeight - 2 * v
        return 0


s = Solution()
print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeightII([31, 26, 33, 21, 40]))
print(s.lastStoneWeightII([1, 2]))

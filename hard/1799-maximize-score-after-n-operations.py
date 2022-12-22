'''
1799. N 次操作后的最大分数和
困难
41
相关企业
给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。

在第 i 次操作时（操作编号从 1 开始），你需要：

选择两个元素 x 和 y 。
获得分数 i * gcd(x, y) 。
将 x 和 y 从 nums 中删除。
请你返回 n 次操作后你能获得的分数和最大为多少。

函数 gcd(x, y) 是 x 和 y 的最大公约数。

 

示例 1：

输入：nums = [1,2]
输出：1
解释：最优操作是：
(1 * gcd(1, 2)) = 1
示例 2：

输入：nums = [3,4,6,8]
输出：11
解释：最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
示例 3：

输入：nums = [1,2,3,4,5,6]
输出：14
解释：最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

提示：

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
'''
from math import gcd
from typing import List
'''
[TOC]

# 思路
动态规划 状态压缩

# 解题方法
一共有2^2n个状态，每次往状态里添加2bit1，计算此时的分数。

设数组dp[2^2n]，dp[status]是第status种状态时的得分，status为整数，含有偶数个bit1，状态转移方程为：
> dp[status] = max(dp[j]),j为status去掉2个bit1的状态

还有各种优化技巧，详见代码

# 复杂度
- 时间复杂度: 
> $O(2^(2n))$ 

- 空间复杂度: 
> $O(2^(2n))$
'''


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        # 将每1bit对应的整数保存到哈希表中缓存
        bitNum = {}
        for i in range(n):
            bitNum[1 << i] = nums[i]
        # 将任意2个整数的gcd放入哈希表缓存
        gcdBuffer = {}
        for i in range(n):
            for j in range(i + 1, n):
                if i == j:
                    continue
                gcdBuffer[(1 << i) | (1 << j)] = gcd(nums[i], nums[j])
        dp = [0] * (2**n)
        # 根据状态含有的1的个数进行分组，下标为1的个数的2倍
        bitList = [[] for _ in range(n // 2 + 1)]
        for i in range(2**n):
            bitcount = i.bit_count()
            if bitcount & 1 == 0:
                bitList[bitcount // 2].append(i)
        # 按照含有的1的个数，从少到多进行遍历
        for idx, statuses in enumerate(bitList[1:]):
            idx += 1
            for status in statuses:
                # 将status中所有的1挑选出来放入bits
                bits = []
                for i in range(n):
                    if (1 << i) & status:
                        bits.append(1 << i)
                # 遍历任意去掉2个bit后的结果
                for i in range(len(bits)):
                    for j in range(i + 1, len(bits)):
                        if i == j:
                            continue
                        remove2bit = bits[i] | bits[j]
                        dp[status] = max(dp[status], dp[remove2bit ^ status] + idx * gcdBuffer[remove2bit])
        return dp[-1]


s = Solution()
assert s.maxScore([1, 2]) == 1
assert s.maxScore([3, 4, 6, 8]) == 11
assert s.maxScore([1, 2, 3, 4, 5, 6]) == 14

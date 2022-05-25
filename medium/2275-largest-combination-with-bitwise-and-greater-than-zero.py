'''
2275. 按位与结果大于零的最长组合
对数组 nums 执行 按位与 相当于对数组 nums 中的所有整数执行 按位与 。

例如，对 nums = [1, 5, 3] 来说，按位与等于 1 & 5 & 3 = 1 。
同样，对 nums = [7] 而言，按位与等于 7 。
给你一个正整数数组 candidates 。计算 candidates 中的数字每种组合下 按位与 的结果。 candidates 中的每个数字在每种组合中只能使用 一次 。

返回按位与结果大于 0 的 最长 组合的长度。

 

示例 1：

输入：candidates = [16,17,71,62,12,24,14]
输出：4
解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。
组合长度是 4 。
可以证明不存在按位与结果大于 0 且长度大于 4 的组合。
注意，符合长度最大的组合可能不止一种。
例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。
示例 2：

输入：candidates = [8,8]
输出：2
解释：最长组合是 [8,8] ，按位与结果 8 & 8 = 8 > 0 。
组合长度是 2 ，所以返回 2 。
 

提示：

1 <= candidates.length <= 105
1 <= candidates[i] <= 107
'''

from typing import List
'''
思路：位运算
一个组合的按位与如果想要大于0，这些数值至少有相同的1位都是1。
可以遍历每一位，统计该位上有多少个数值是1，该位上是1的数值可以构成组合。
因为candidates[i] <= 10^7，所以只需要统计24位即可，因为2^24>10^7。

时间复杂度：O(24*n)
空间复杂度：O(1)
'''


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(24):
            count, d = 0, 1 << i
            for num in candidates:
                count += 1 if d & num else 0
            ans = max(ans, count)
        return ans

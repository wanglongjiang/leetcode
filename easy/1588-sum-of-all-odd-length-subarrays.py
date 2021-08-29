'''
1588. 所有奇数长度子数组的和
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。



示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：

输入：arr = [10,11,12]
输出：66


提示：

1 <= arr.length <= 100
1 <= arr[i] <= 1000
'''
from typing import List
'''
思路：滑动窗口
设n为arr.length,遍历<=n的所有奇数，将其作为滑动窗口大小，合计所有滑动窗口的和

时间复杂度：O(n^2)
空间复杂度：O(1)
'''


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1, n + 1, 2):  # 遍历n以内的所有奇数
            s = 0
            for j in range(i):  # 初始化窗口值
                s += arr[j]
            ans += s
            left, right = 0, i
            while right < n:
                s = s + arr[right] - arr[left]  # 计算下一个滑动窗口值
                ans += s
                left += 1
                right += 1
        return ans

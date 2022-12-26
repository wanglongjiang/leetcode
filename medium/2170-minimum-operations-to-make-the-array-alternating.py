'''
2170. 使数组变成交替数组的最少操作数
给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。

如果满足下述条件，则数组 nums 是一个 交替数组 ：

nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。

返回使数组变成交替数组的 最少操作数 。

 

示例 1：

输入：nums = [3,1,3,2,4,3]
输出：3
解释：
使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。
在这种情况下，操作数为 3 。
可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。
示例 2：

输入：nums = [1,2,2,2,2]
输出：2
解释：
使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1].
在这种情况下，操作数为 2 。
注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''
from typing import Counter, List
'''
思路：贪心 哈希
分别统计奇数下标上的数值、和偶数下标上的数值哪个多，保留最多的1个作为奇数上和偶数上的（注意不能相同）
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 1 if nums[0] == nums[1] else 0
        oddCount, evenCount = Counter(), Counter()
        for i in range(n):
            if i & 1:
                oddCount[nums[i]] += 1
            else:
                evenCount[nums[i]] += 1
        oddTop2, evenTop2 = oddCount.most_common(2), evenCount.most_common(2)  # 分别获取最多的2个
        oddMax1, oddMax1Count, oddMax2Count = oddTop2[0][0], oddTop2[0][1], oddTop2[1][1] if len(oddTop2) == 2 else 0
        evenMax1, evenMax1Count, evenMax2Count = evenTop2[0][0], evenTop2[0][1], evenTop2[1][1] if len(evenTop2) == 2 else 0
        if oddMax1 != evenMax1:  # 奇数和偶数下标的最多元素不是同一个,都保留最多的那个即可
            return n - oddMax1Count - evenMax1Count
        else:  # 奇数、偶数下标最多的元素相同，挑选变动较少的一个组合
            return n - max(oddMax1Count + evenMax2Count, oddMax2Count + evenMax1Count)


s = Solution()
print(s.minimumOperations([3, 1, 3, 2, 4, 3]))
print(s.minimumOperations([1, 2, 2, 2, 2]))

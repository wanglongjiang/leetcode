'''
2449. 使数组相似的最少操作次数
给你两个正整数数组 nums 和 target ，两个数组长度相等。

在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：

令 nums[i] = nums[i] + 2 且
令 nums[j] = nums[j] - 2 。
如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。

请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。

 

示例 1：

输入：nums = [8,12,6], target = [2,14,10]
输出：2
解释：可以用两步操作将 nums 变得与 target 相似：
- 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
- 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
2 次操作是最少需要的操作次数。
示例 2：

输入：nums = [1,2,5], target = [4,1,3]
输出：1
解释：一步操作可以使 nums 变得与 target 相似：
- 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。
示例 3：

输入：nums = [1,1,1,1,1], target = [1,1,1,1,1]
输出：0
解释：数组 nums 已经与 target 相似。
 

提示：

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
nums 一定可以变得与 target 相似。
'''
from typing import List
'''
天之道，损有余而补不足
由题目得知，每次操作是修改nums的任意2个元素，将一个元素-2另一个元素+2
题目又告知nums一定可以变成target，那么nums中偶数、奇数的个数与target中偶数、奇数的个数是一样多的。
分别排序2个数组的奇数、偶数，再分别对比，找到所有nums比target小的那部分的差。
少的那部分差肯定是个偶数，将其除以2，即为需要操作的次数

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # 数组拆分成奇数和偶数
        numsEven, numsOdd, targetEven, targetOdd = [], [], [], []
        for i in range(len(nums)):
            if nums[i] & 1:
                numsOdd.append(nums[i])
            else:
                numsEven.append(nums[i])
            if target[i] & 1:
                targetOdd.append(target[i])
            else:
                targetEven.append(target[i])
        # 排序
        numsEven.sort()
        numsOdd.sort()
        targetEven.sort()
        targetOdd.sort()
        # 合计差
        ans = 0
        for i in range(len(numsEven)):
            if numsEven[i] < targetEven[i]:
                ans += targetEven[i] - numsEven[i]
        for i in range(len(numsOdd)):
            if numsOdd[i] < targetOdd[i]:
                ans += targetOdd[i] - numsOdd[i]
        return ans >> 1


s = Solution()
assert s.makeSimilar(nums=[8, 12, 6], target=[2, 14, 10]) == 2
assert s.makeSimilar(nums=[1, 1, 1, 1, 1], target=[1, 1, 1, 1, 1]) == 0
assert s.makeSimilar(nums=[1, 2, 5], target=[4, 1, 3]) == 1

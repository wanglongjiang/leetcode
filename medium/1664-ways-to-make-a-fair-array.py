'''
1664. 生成平衡数组的方案数
给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果 nums = [6,1,7,4,1] ，那么：

选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。

请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。

 

示例 1：

输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。
示例 2：

输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。
示例 3：

输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
'''
from typing import List
'''
后缀和
首先求数组的奇数、偶数后缀和
然后遍历所有下标，求出删除该下标元素后的奇数和、偶数和

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 1
        # 计算奇数、偶数后缀和
        postfixSum = nums.copy()
        for i in range(n - 3, -1, -1):
            postfixSum[i] += postfixSum[i + 2]
        ans = 0
        # 删掉1个元素后，计算是否平衡
        for i in range(n - 2):
            if i & 1:  # i为奇数下标，需要将总奇数和-i及之后的奇数和+i之后的偶数和，总偶数和-i之后的偶数和+i之后的奇数和。然后判断是否平衡
                ans += postfixSum[0] - postfixSum[i + 1] + postfixSum[i + 2] == postfixSum[1] - postfixSum[i] + postfixSum[i + 1]
            else:  # i为偶数下标，需要将总奇数和-i之后的奇数和+i之后的偶数和，总偶数和-i及之后的偶数和+i之后的奇数和
                ans += postfixSum[0] - postfixSum[i] + postfixSum[i + 1] == postfixSum[1] - postfixSum[i + 1] + postfixSum[i + 2]
        if n & 1:
            ans += postfixSum[0] - postfixSum[n - 1] == postfixSum[1]  # 总长度为奇数，删掉最后一个下标，实际上是偶数和减去最后一个，判断是否平衡
            ans += postfixSum[0] - postfixSum[n - 1] == postfixSum[1] - postfixSum[n - 2] + postfixSum[n - 1]  # 总长度为奇数，删掉倒数第2个，偶数和需要减去最后一个，奇数和需要加上最后一个，删掉倒数第2个
        else:  # 总长度为偶数，与上面的同理进行计算
            ans += postfixSum[0] == postfixSum[1] - postfixSum[n - 1]
            ans += postfixSum[0] - postfixSum[n - 2] + postfixSum[n - 1] == postfixSum[1] - postfixSum[n - 1]
        return ans


s = Solution()
print(s.waysToMakeFair([1, 1, 1, 1, 1]))
print(s.waysToMakeFair([1]))
print(s.waysToMakeFair([2, 1, 6, 4]))
print(s.waysToMakeFair([1, 1, 1]))
print(s.waysToMakeFair([1, 2, 3]))

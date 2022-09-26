'''
6190. 找到所有好下标
给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。

对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：

下标 i 之前 的 k 个元素是 非递增的 。
下标 i 之后 的 k 个元素是 非递减的 。
按 升序 返回所有好下标。

 

示例 1：

输入：nums = [2,1,1,1,3,4,1], k = 2
输出：[2,3]
解释：数组中有两个好下标：
- 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
- 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
示例 2：

输入：nums = [2,1,1,2], k = 2
输出：[]
解释：数组中没有好下标。
 

提示：

n == nums.length
3 <= n <= 105
1 <= nums[i] <= 106
1 <= k <= n / 2
'''
from typing import List
'''
思路：前缀和
首先进行预处理，用2个数组分别记录截止下标i，它前面的非递增子数组的长度和它后面非递减子数组的长度。
然后从k开始，检查下标前面和后面的子数组的非递增和非递减长度是否满足要求。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        noinc, nodec = [1] * n, [1] * n
        noinc[0] = 0
        nodec[-1] = 0
        for i in range(2, n):
            if nums[i - 1] <= nums[i - 2]:
                noinc[i] = noinc[i - 1] + 1
        for i in range(n - 3, -1, -1):
            if nums[i + 1] <= nums[i + 2]:
                nodec[i] = nodec[i + 1] + 1
        ans = []
        for i in range(k, n - k):
            if noinc[i] >= k and nodec[i] >= k:
                ans.append(i)
        return ans


s = Solution()
print(s.goodIndices(nums=[2, 1, 1, 1, 3, 4, 1], k=2))
print(s.goodIndices([878724, 201541, 179099, 98437, 35765, 327555, 475851, 598885, 849470, 943442], 4))
print(s.goodIndices(nums=[2, 1, 1, 2], k=2))

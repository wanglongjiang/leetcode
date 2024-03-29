'''
532. 数组中的 k-diff 数对
给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
注意，|val| 表示 val 的绝对值。



示例 1：

输入：nums = [3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
示例 2：

输入：nums = [1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
示例 3：

输入：nums = [1, 3, 1, 5, 4], k = 0
输出：1
解释：数组中只有一个 0-diff 数对，(1, 1)。
示例 4：

输入：nums = [1,2,4,4,3,3,0,9,2,3], k = 3
输出：2
示例 5：

输入：nums = [-1,-2,-3], k = 1
输出：2


提示：

1 <= nums.length <= 10^4
-10^7 <= nums[i] <= 10^7
0 <= k <= 10^7
'''
from typing import List
'''
思路：哈希
设2个哈希表，用于保存nums中的数字、数对
遍历nums，对于每个数字nums[i]，先查找哈希表中nums[i]+k及nums[i]-k，并记录到结果哈希表中，然后将当前数值加入哈希表

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numSet, pairSet = set(), set()
        for num in nums:
            if (num - k) in numSet:
                pairSet.add((num - k, num))
            if (num + k) in numSet:
                pairSet.add((num, num + k))
            numSet.add(num)
        return len(pairSet)


s = Solution()
print(s.findPairs(nums=[3, 1, 4, 1, 5], k=2))
print(s.findPairs(nums=[1, 2, 3, 4, 5], k=1))
print(s.findPairs(nums=[1, 3, 1, 5, 4], k=0))
print(s.findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3))
print(s.findPairs(nums=[-1, -2, -3], k=1))

'''
和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。

 

示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15
 

提示：

1 <= nums.length <= 3 * 10^4
nums[i] 不是 0 就是 1
0 <= goal <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：前缀数组 哈希
计算截止每个索引的前缀和prefixSum，保存到哈希表中计数。
如果a=prefixSum-goal在哈希表中存在，说明前缀和为a的下标和当前下标构成的子数组和为goal满足要求。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumSet = defaultdict(int)
        prefixSum = 0
        ans = 0
        for num in nums:
            prefixSum += num
            if prefixSum == goal:
                ans += 1
            a = prefixSum - goal
            if a in prefixSumSet:
                ans += prefixSumSet[a]
            prefixSumSet[prefixSum] += 1
        return ans


s = Solution()
print(s.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(s.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))

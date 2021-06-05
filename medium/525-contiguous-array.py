'''
连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1
'''
from typing import List
'''
思路：前缀和+哈希
如果将0视为-1，题目就是求和为0的最长子数组。
1. 遍历数组，将0视为1之后求前缀和sums，然后将前缀和的索引记录到哈希表中，如果遇到前缀和相同的情况下，只需要记录索引最小的
2. 从右向左遍历前缀和，
> 如果前缀和sums[i]为0，此时的索引i即为子数组长度
> 如果前缀和sums[i]不为0，在哈希表中查找值为sums[i]是否存在，如果存在，这2个索引直接的差即为子数组长度

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        sums[0] = 1 if nums[0] else -1
        idxMap = {sums[0]: 0}
        for i in range(1, n):
            sums[i] = sums[i - 1] + (1 if nums[i] else -1)  # 求前缀和
            if sums[i] not in idxMap:  # 将索引最小的值记录下来
                idxMap[sums[i]] = i
        maxLen = 0
        for i in range(n - 1, -1, -1):
            if i < maxLen:  # 如果索引已经小于当前得到的最长子数组大小，不需要继续查找了
                break
            if sums[i] == 0:
                maxLen = i + 1
            elif sums[i] in idxMap:  # 如果与当前前缀同值的索引存在，当前数组减去找到的数组和为0
                maxLen = max(maxLen, i - idxMap[sums[i]])
        return maxLen


s = Solution()
print(s.findMaxLength([0, 0, 1]))
print(s.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))
print(s.findMaxLength([0, 1]))
print(s.findMaxLength([0, 1, 0]))

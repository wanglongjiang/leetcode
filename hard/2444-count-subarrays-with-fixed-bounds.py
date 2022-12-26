'''
2444. 统计定界子数组的数目
给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

nums 的定界子数组是满足下述条件的一个子数组：

子数组中的 最小值 等于 minK 。
子数组中的 最大值 等于 maxK 。
返回定界子数组的数目。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
示例 2：

输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
 

提示：

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
'''
from typing import List
'''
思路：一次遍历
设一个变量leftLimit，保存不满足>=minK，<=maxK的左边界
设变量minIndex和maxIndex保存leftLimit最右边minK和maxK的下标
遍历nums，对于当前坐标i，min(minIndex,maxIndex)左边，leftLimit右边所有下标，都可以与i形成满足要求的子数组。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans, leftLimit, minIndex, maxIndex = 0, -1, -1, -1
        for i in range(len(nums)):
            leftLimit = i if nums[i] < minK or nums[i] > maxK else leftLimit
            minIndex = i if nums[i] == minK else minIndex
            maxIndex = i if nums[i] == maxK else maxIndex
            ans += max(0, min(minIndex, maxIndex) - leftLimit)
        return ans

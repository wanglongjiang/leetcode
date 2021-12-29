'''
1995. 统计特殊四元组
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d
 

示例 1：

输入：nums = [1,2,3,6]
输出：1
解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
示例 2：

输入：nums = [3,3,6,4,5]
输出：0
解释：[3,3,6,4,5] 中不存在满足要求的四元组。
示例 3：

输入：nums = [1,1,1,3,5]
输出：4
解释：满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
 

提示：

4 <= nums.length <= 50
1 <= nums[i] <= 100
'''

from typing import List
'''
思路：四重循环，暴力组合
用三重循环迭代3个变量之和，如果和在剩余数组中存在，则是满足要求的4元组

时间复杂度：O(n^4)
空间复杂度：O(n)
'''


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        allnums = set(nums)
        ans = 0
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    s = nums[i] + nums[j] + nums[k]
                    if s in allnums:
                        for l in range(k + 1, len(nums)):
                            if nums[l] == s:
                                ans += 1
        return ans


s = Solution()
print(s.countQuadruplets([28, 8, 49, 85, 37, 90, 20, 8]))
print(s.countQuadruplets([9, 6, 8, 23, 39, 23]))

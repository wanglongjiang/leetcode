'''
剑指 Offer II 007. 数组中和为 0 的三个数
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
 

注意：本题与主站 15 题相同：https://leetcode-cn.com/problems/3sum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1fGaJU
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序、双指针
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        numsLen = len(nums)
        nums.sort()
        for left in range(numsLen - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            right = numsLen - 1
            target = -nums[left]
            for mid in range(left + 1, right):
                if mid > left + 1 and nums[mid] == nums[mid - 1]:
                    continue
                while mid < right and nums[mid] + nums[right] > target:
                    right -= 1
                if mid == right:
                    break
                if nums[mid] + nums[right] == target:
                    result.append([nums[left], nums[mid], nums[right]])
        return result

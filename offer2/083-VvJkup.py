'''
剑指 Offer II 083. 没有重复元素集合的全排列
给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
 

注意：本题与主站 46 题相同：https://leetcode-cn.com/problems/permutations/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/VvJkup
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
'''
解题思路：回溯搜索
用回溯，生成全排列

时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def perm(index):
            if index == len(nums):
                result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                perm(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        perm(0)
        return result

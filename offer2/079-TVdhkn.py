'''
剑指 Offer II 079. 所有子集
给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
 

注意：本题与主站 78 题相同： https://leetcode-cn.com/problems/subsets/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/TVdhkn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：回溯查找所有组合
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        comb = []
        n = len(nums)

        def backtrack(index: int, k: int):
            if len(comb) == k:
                ans.append(comb.copy())
            for i in range(index, n):
                comb.append(nums[i])
                backtrack(i + 1, k)
                comb.pop()

        for i in range(len(nums) + 1):
            backtrack(0, i)
        return ans

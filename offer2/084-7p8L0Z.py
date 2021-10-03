'''
剑指 Offer II 084. 含有重复元素集合的全排列
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
 

注意：本题与主站 47 题相同： https://leetcode-cn.com/problems/permutations-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/7p8L0Z
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
解题思路：回溯
回溯搜索，插入结果集之前进行重复判定。
重复判定使用set进行排重

时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        unionSet = set()
        nums.sort()

        def perm(index):
            if index == len(nums):
                key = ''.join(map(str, nums))
                if key not in unionSet:
                    unionSet.add(key)
                    result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                perm(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        perm(0)
        return result

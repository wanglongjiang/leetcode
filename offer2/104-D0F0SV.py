'''
剑指 Offer II 104. 排列的数目
给定一个由 不同 正整数组成的数组 nums ，和一个目标整数 target 。请从 nums 中找出并返回总和为 target 的元素组合的个数。
数组中的数字可以在一次排列中出现任意次，但是顺序不同的序列被视作不同的组合。

题目数据保证答案符合 32 位整数范围。

 

示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000
 

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

 

注意：本题与主站 377 题相同：https://leetcode-cn.com/problems/combination-sum-iv/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/D0F0SV
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：回溯
1、数组排序
2、回溯函数每层依次减去一个数，如果大于0，继续回溯，如果=0，有合法的解，如果>0，结束当前回溯
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mem = {}

        def backtrack(target):
            if target in mem:
                return mem[target]
            ans = 0
            for i in range(n):
                if nums[i] < target:
                    ans += backtrack(target - nums[i])
                elif nums[i] == target:
                    ans += 1
                else:
                    break
            mem[target] = ans
            return ans

        return backtrack(target)

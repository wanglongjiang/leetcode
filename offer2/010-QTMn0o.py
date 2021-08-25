'''
剑指 Offer II 010. 和为 k 的子数组
给定一个正整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。

 

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2
解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
示例 2 :

输入:nums = [1,2,3], k = 3
输出: 2
 

提示:

1 <= nums.length <= 2 * 10^4
1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

 

注意：本题与主站 560 题相同： https://leetcode-cn.com/problems/subarray-sum-equals-k/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/QTMn0o
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：前缀和+哈希
依次从左到右计算前缀和，如果前缀和presum = k，则满足要求的子数组数量ans+1
如果以往的子数组前缀和等于presum-k，因为以往的子数组是从0..x,而当前前缀和是从0..i，i>x，必然有当前子数组前缀和减去满足该条件的子数组前缀和为k
以往的子数组前缀和用一个哈希表presums记录，key为前缀和，value为具有该前缀和的子数组个数

 1074.[元素和为目标值的子矩阵数量](hard/1074-number-of-submatrices-that-sum-to-target.py)是这道题的升级版

 时间复杂度：O(n)
 空间复杂度：O(n)
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = 0  # 前缀和
        presums = defaultdict(int)  # 用于记录前缀和个数
        for num in nums:
            presum += num
            if presum == k:  # 数组的前缀和为k，满足要求
                ans += 1
            if (presum - k) in presums:  # 当前数组减去以往所有前缀和为presum-k的子数组，都会满足要求
                ans += presums[presum - k]
            presums[presum] += 1
        return ans

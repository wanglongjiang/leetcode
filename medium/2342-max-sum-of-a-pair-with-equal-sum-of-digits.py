'''
2342. 数位和相等数对的最大和
给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），
且 nums[i] 的数位和 与  nums[j] 的数位和相等。

请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。

 

示例 1：

输入：nums = [18,43,36,13,7]
输出：54
解释：满足条件的数对 (i, j) 为：
- (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
- (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
所以可以获得的最大和是 54 。
示例 2：

输入：nums = [10,12,19,14]
输出：-1
解释：不存在满足条件的数对，返回 -1 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import List
'''
思路：哈希
设一个哈希表，key为数位和，value为相同数位和最大的数值
遍历所有数字，计算与其相同数位和的和，找到最大的一个
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        ans, sumhash = -1, {}
        for num in nums:
            sd = sumOfDigits(num)
            if sd not in sumhash:
                sumhash[sd] = num
            else:
                ans = max(ans, num + sumhash[sd])
                if sumhash[sd] < num:
                    sumhash[sd] = num
        return ans


s = Solution()
print(s.maximumSum([18, 43, 36, 13, 7]))

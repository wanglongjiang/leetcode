'''
945. 使数组唯一的最小增量
中等
222
相关企业
给你一个整数数组 nums 。每次 move 操作将会选择任意一个满足 0 <= i < nums.length 的下标 i，并将 nums[i] 递增 1。

返回使 nums 中的每个值都变成唯一的所需要的最少操作次数。

 

示例 1：

输入：nums = [1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2：

输入：nums = [3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
 

提示：
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''
from typing import List
'''
[TOC]

# 思路
贪心

# 解题方法
1. 排序nums
2. 设置一个数值unuseNum，该数值为nums中最小的未出现过的数，例如[1,2,4,5,7]，最小未使用的数就是3，如果nums中没有未使用的数，那么unuseNum为最大值+1
3. 遍历nums，如果当前nums[i]值与前面的重复，需要将其设置为unuseNum，累计其中的差额，unuseNum也需要寻找下一个未使用数

# 复杂度
- 时间复杂度: 
> $O(nlog(n))$ 排序需要O(nlog(n))时间，第3步遍历nums，最多有2个指针分别遍历一次

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        unuseNum, j, n = nums[0], 0, len(nums)
        ans = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                if unuseNum <= nums[i] or unuseNum == nums[j]:
                    # 搜寻下一个未使用的数值
                    for k in range(max(j + 1, i + 1), n):
                        if nums[k] - 1 > nums[k - 1]:  # nums[k]和nums[k-1]之间有空位，nums[k - 1] + 1未出现过，将其赋值给unuseNum待用
                            j = k
                            unuseNum = nums[k - 1] + 1
                            break
                    else:  # 整个nums遍历完未找到，未使用的数值即为最大值+1
                        unuseNum = nums[-1] + 1
                        j = n - 1
                ans += unuseNum - nums[i]  # 将nums[i]变为unuseNum即为最少操作
                unuseNum += 1
        return ans


s = Solution()
assert s.minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6
assert s.minIncrementForUnique([0, 2, 2]) == 1
assert s.minIncrementForUnique([1, 2, 2]) == 1

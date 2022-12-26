'''
915. 分割数组
给定一个数组 A，将其划分为两个连续子数组 left 和 right， 使得：

left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 的长度要尽可能小。
在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。



示例 1：

输入：[5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
示例 2：

输入：[1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]


提示：

2 <= A.length <= 30000
0 <= A[i] <= 10^6
可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。
'''
from typing import List
'''
思路：后缀数组
题目是求left的最大值<=right的最小值。
可以设辅助数组rightMin[n]
rightMin[i]=min(nums[i]..nums[n-1])
从左到右遍历nums，并用一个leftMax记录left部分最大的值，如果遍历过程中发现leftMax>=rightMin[i]那么此时i即为left，right的分隔

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        rightMin = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            rightMin[i] = min(rightMin[i], rightMin[i + 1])
        leftMax = nums[0]
        for i in range(1, len(nums)):
            if leftMax <= rightMin[i]:
                return i
            leftMax = max(leftMax, nums[i])


s = Solution()
print(s.partitionDisjoint([32, 57, 24, 19, 0, 24, 49, 67, 87, 87]) == 7)  # TODO
print(s.partitionDisjoint([5, 0, 3, 8, 6]))
print(s.partitionDisjoint([1, 1, 1, 0, 6, 12]))

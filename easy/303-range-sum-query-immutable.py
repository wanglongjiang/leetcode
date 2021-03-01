'''
区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
'''
from typing import List
'''
思路：简单的迭代求和
'''


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.sums[i] = nums[i]
            else:
                self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]


n = NumArray([-2, 0, 3, -5, 2, -1])
print(n.sumRange(0, 2))
print(n.sumRange(2, 5))
print(n.sumRange(0, 5))

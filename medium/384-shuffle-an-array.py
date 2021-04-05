'''
打乱数组
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
'''
from typing import List
'''
思路：用1个数组保存原始数组。
每次shuffle都会调用n次随机交换2个元素
'''


class Solution:
    def __init__(self, nums: List[int]):
        self.org = list(nums)
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.org

    def shuffle(self) -> List[int]:
        import random
        n = self.n
        for i in range(random.randint(1, min(1, n // 2))):
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

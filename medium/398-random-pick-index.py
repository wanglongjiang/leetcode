'''
398. 随机数索引
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);
'''
from typing import List
from collections import defaultdict
import random
'''
思路：水塘抽样
根据题意，这个题目是空间敏感，pick时遍历所有的target，将其加入list，然后随机选择一个

'''


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = defaultdict(list)

    def pick(self, target: int) -> int:
        if target not in self.map:
            li = []
            self.map[target] = li
            for i, num in enumerate(self.nums):
                if num == target:
                    li.append(i)
        return random.choice(self.map[target])

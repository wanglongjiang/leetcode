'''
区域和检索 - 数组可修改
给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。

实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值更新为 val
int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和
（即，nums[left] + nums[left + 1], ..., nums[right]）

提示：

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
最多调用 3 * 10^4 次 update 和 sumRange 方法
'''

from typing import List
'''
思路：树状数组
用树状数组存储数组前缀和
时间复杂度：update为O(logn)，sumRange为O(logn)，初始化为O(nlogn)
'''


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.c = [0] * (self.n + 1)
        for i in range(self.n):
            self.realUpdate(i, nums[i])

    def lowbit(self, i):
        return i & -i

    def getSum(self, i):
        res = 0
        while i > 0:
            res += self.c[i]
            i -= self.lowbit(i)
        return res

    def realUpdate(self, index: int, val: int) -> None:
        index += 1
        while index <= self.n:
            self.c[index] += val
            index += self.lowbit(index)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.realUpdate(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        leftSum = 0
        if left > 0:
            leftSum = self.getSum(left)
        return self.getSum(right + 1) - leftSum


numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))  # 返回 9 ，sum([1,3,5]) = 9
numArray.update(1, 2)  # nums = [1,2,5]
print(numArray.sumRange(0, 2))  # 返回 8 ，sum([1,2,5]) = 8

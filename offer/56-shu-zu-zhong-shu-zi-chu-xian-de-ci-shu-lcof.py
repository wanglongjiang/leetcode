'''
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，
空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

限制：

2 <= nums.length <= 10000
'''
from typing import List
'''
思路：随机分区+异或
使用快排里面的思路，选择1个数pivot作为基准，将数组分为>=pivot和<pivot的2部分，
先对>pivot的进行异或，如果结果为0，则2个数出现在<pivot的部分里面
    如果结果不为0，对<pivot的部分进行异或，如果异或结果为0，则2个数出现在>=pivot的部分
        如果结果为不为0，2个数组的异或结果即为2个数。
    经过上面的判断，2个数出现在<pivot或者>=pivot的部分，需要缩小范围，继续查找，直至数组大小为0，直接返回这2个数
时间复杂度：O(n)，分区函数时间复杂度O(logn)最坏情况下会执行logn次
空间复杂度:O(1)
'''


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        import random

        def xor(start, end):
            ans = nums[start]
            for i in range(start + 1, end):
                ans ^= nums[i]
            return ans

        def part(start, end):
            if end - start == 2:
                return [nums[start], nums[start + 1]]
            k = random.randint(start, end - 1)
            nums[start], nums[k] = nums[k], nums[start]
            pivot = nums[start]
            i, j = start, end - 1
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            if i == start or i == end:  # 选择的pivot未能将数组分成2个区，继续分区
                return part(start, end)
            lowSize = i - start  # 小于pivot的分区大小
            if lowSize & 1 == 1:  # 分区大小为奇数，2个数分别位于2个分区内，用异或将结果计数出
                return [xor(start, i), xor(i, end)]
            lowXor = xor(start, i)
            if lowXor:
                highXor = xor(i, end)
                if highXor:  # 如果2个分区的异或都不为空，结果就是2个分区的异或结果
                    return [lowXor, highXor]
                return part(start, i)  # 高分区异或结果为0，2个数在低分区内
            return part(i, end)  # 低分区异或结果为0，2个数在高分区内

        return part(0, len(nums))


s = Solution()
print(s.singleNumbers([4, 1, 4, 6]))
print(s.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))

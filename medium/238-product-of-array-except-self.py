'''
除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''
from typing import List
'''
思路1，动态规划。
1个数组leftProduct存储从左到右的所有数的乘积，另外1个数组rightProduct存储从右到左的所有数的乘积
第i个结果为leftProduct[i-1]*rightProduct[n-i+1]
时间复杂度：O(n)
空间复杂度：O(1)

思路2，动态规划(常数空间)
对上面的算法的空间复杂度进行优化
1、首先使用返回结果output存储从右到左所有数的乘积
2、从左往右遍历nums用1个变量leftProduct累计乘积，并与ouput中的从右到左的乘积相乘
'''


class Solution:
    # 思路2
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        output[-1] = nums[-1]
        for i in range(n - 2, 0, -1):
            output[i] = output[i + 1] * nums[i]
        leftProduct = 1
        for i in range(0, n - 1):
            output[i] = leftProduct * output[i + 1]
            leftProduct *= nums[i]
        output[-1] = leftProduct
        return output

    # 思路1
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProduct, rightProduct = [0] * n, [0] * n
        leftProduct[0] = nums[0]
        rightProduct[-1] = nums[-1]
        for i in range(1, n):
            leftProduct[i] = leftProduct[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i]
        output = [0] * n
        output[0] = rightProduct[1]
        output[-1] = leftProduct[-2]
        for i in range(1, n - 1):
            output[i] = leftProduct[i - 1] * rightProduct[i + 1]
        return output


s = Solution()
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
print(s.productExceptSelf([1, 2, 3, 4]))

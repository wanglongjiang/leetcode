'''
汉明距离总和
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。
'''
from typing import List
'''
思路1，回溯遍历数组中所有元素的组合，求其异或的1的个数（n&(n-1))
时间复杂度：O(n^2)
思路2，回溯遍历数组中所有元素的组合，求其异或的1的个数(jdk类库算法)
时间复杂度：O(n^2)
'''


class Solution:
    # 思路1
    def totalHammingDistance1(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                num = nums[i] ^ nums[j]
                while num > 0:
                    count += 1
                    num &= (num - 1)
        return count

    # 思路2
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        # 这个函数就是jdk里面的bigCount
        def bitCount(i):
            i = i - ((i >> 1) & 0x55555555)
            i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
            i = (i + (i >> 4)) & 0x0f0f0f0f
            i = i + (i >> 8)
            i = i + (i >> 16)
            return i & 0x3f

        for i in range(n - 1):
            for j in range(i + 1, n):
                count += bitCount(nums[i] ^ nums[j])
        return count


s = Solution()
print(s.totalHammingDistance2([4, 14, 2]))

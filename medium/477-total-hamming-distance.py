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
思路3，1次遍历所有位上的1的个数。只有0和1的异或才是1，所以对于每1位来说，只有与0其相反的位的组合才是有意义的。可以统计每位上1的个数count
然后这个位上产生的异或的1个个数是count*(n-count)。再合计32位上所有异或的数量。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * 32
        for num in nums:
            for j in range(32):
                if num & 1:
                    count[j] += 1
                num >>= 1
                if num == 0:
                    break
        ans = 0
        for i in range(32):
            ans += count[i] * (n - count[i])
        return ans

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
    def totalHammingDistance2(self, nums: List[int]) -> int:
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

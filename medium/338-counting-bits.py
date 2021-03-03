'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
'''

from typing import List
'''
思路：
很容易给出O(n*sizeof(int))的算法，想优化成O(n)。
优化成O(n)的算法，需要利用动态规划
'''


class Solution:
    def countBitsOld(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(num + 1):
            count = 0
            for j in range(32):
                if (i >> j) & 0x1 == 1:
                    count += 1
                if (i >> j) == 0:
                    break
            ans[i] = count
        return ans

    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans


s = Solution()
print(s.countBits(9))
print(s.countBits(2))

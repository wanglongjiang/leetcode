'''
和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''
from typing import List
from collections import Counter
'''
思路：数学（同余） 哈希 前缀和
计算数组的前缀和presum，再计算前缀和与k的余数r=presum mod k
根据同余定理，如果有presum[i]%k == presum[j]%k，则子数组i+1..j的和能整除k

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = Counter()
        remainders[0] = 1
        presum, ans = 0, 0
        for num in nums:
            presum += num
            r = presum % k
            if r in remainders:
                ans += remainders[r]  # 所有余数为r的子数组右边界，与当前坐标构成的子数组和都是k
            remainders[r] += 1
        return ans


s = Solution()
print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

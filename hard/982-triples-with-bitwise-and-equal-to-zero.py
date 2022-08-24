'''
982. 按位与为零的三元组
给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 
示例 1：

输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
示例 2：

输入：nums = [0,0,0]
输出：27
 

提示：

1 <= nums.length <= 1000
0 <= nums[i] < 2^16
'''

from collections import defaultdict
from typing import Counter, List
'''
思路：哈希
1、用2重循环，计算所有2个数字的按位与，并保存到哈希表中计数，此次操作时间复杂度O(n^2)。因为nums[i]<2^16，故哈希表中所有的key最多有2^16个
2、遍历nums所有数字，再遍历哈希表中所有key，当num、key按位与结果为0，三元组数量+二者乘积

时间复杂度：O(n^2+min(2^16,n^2)*n)
空间复杂度：O(n^2)
'''


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        ijCount = defaultdict(int)
        for numi, counti in numCount.items():
            for numj, countj in numCount.items():
                ijCount[numi & numj] += counti * countj
        ans = 0
        for num, count in numCount.items():
            for ij, countij in ijCount.items():
                if num & ij == 0:
                    ans += count * countij
        return ans


s = Solution()
print(s.countTriplets([2, 1, 3]))
print(s.countTriplets([0, 0, 0]))

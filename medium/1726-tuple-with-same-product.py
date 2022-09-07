'''
1726. 同积元组
给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。

 

示例 1：

输入：nums = [2,3,4,6]
输出：8
解释：存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
示例 2：

输入：nums = [1,2,4,5,10]
输出：16
解释：存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums 中的所有元素 互不相同
'''
from math import factorial
from typing import Counter, List
'''
思路：哈希
用2重循环计算任意2个元素的乘积并加入哈希表计数
然后遍历哈希表，计数大于1的乘积代表这里面可以任意挑选2个乘积构成合法的元组，可以用排列公式计算。

时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counter[nums[i] * nums[j]] += 1
        ans = 0
        for count in counter.values():
            if count > 1:
                ans += factorial(count) // factorial(count - 2) * 4
        return ans


s = Solution()
print(s.tupleSameProduct([1, 2, 4, 5, 10]))

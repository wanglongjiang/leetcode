'''
使数组和能被 P 整除
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。

子数组 定义为原数组中连续的一组元素。

 

示例 1：

输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
示例 2：

输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
示例 3：

输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
示例  4：

输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
示例 5：

输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= p <= 10^9
'''
from typing import List
'''
思路：数学 同余定理 哈希
设sum[i]为0..i的前缀和，sum[j]为0..j的前缀和，sum[n]为整个数组的前缀和
如果想要使0..i + j+1..n的数组能整除p，即为(sum[n]-sum[j]+sum[i])%p=0
-> ((sum[n]-sum[j])%p+sum[i]%p)%p=0
-> 即p-(sum[n]-sum[j])%p = sum[i]%p
根据上面的思路写出算法：
1. 遍历每个元素nums[i]，求出当前位置的前缀和prefixSum,和当前位置的余数remainder[i]，并将remainder存入哈希表中
2. 从后往前遍历查找满足remainder[j]-remainder[n]在哈希表中存在，

时间复杂度：O(n)
空间复杂度；O(n)
'''


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res = n = len(nums)
        mod = sum(nums) % p
        if mod == 0:
            return 0
        hashmap = {0: -1}
        sub_mod = 0
        for i, num in enumerate(nums):
            sub_mod = (sub_mod + num) % p
            target = (sub_mod - mod + p) % p
            if target in hashmap:
                res = min(res, i - hashmap[target])
                if res == 1 and res != n:
                    return res
            hashmap[sub_mod] = i
        if res == n:
            res = -1
        return res


s = Solution()
print(s.minSubarray(nums=[3, 1, 4, 2], p=6))
print(s.minSubarray(nums=[6, 3, 5, 2], p=9))
print(s.minSubarray(nums=[1, 2, 3], p=7))
print(s.minSubarray(nums=[1, 2, 3], p=3))
print(s.minSubarray(nums=[1000000000, 1000000000, 1000000000], p=3))

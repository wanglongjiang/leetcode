'''
2488. 统计中位数为 K 的子数组
困难
25
相关企业
给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。

注意：

数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。
 

示例 1：

输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
示例 2：

输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
nums 中的整数互不相同
'''
from collections import defaultdict
from math import factorial
from typing import List
'''
[TOC]

# 思路
前缀和 哈希

# 解题方法
1. 统计截止每个下标的大于k的计数前缀和
> 例如nums = [3,2,1,4,5], k = 4。
> 截止i=4，大于k的计数为1，小于等于k的计数为4

2. 在每个下标处计算key=大于k的计数-小于等于k的计数，将key存储到哈希表中计数

3. 对于某个key，如果其计数>1，说明有若干下标之间的子数组大于k和小于等于k的数量相同，也即满足k为中位数

4. 如果有key1-key2=-1，那么这2个key对应的下标们构成的子数组中大于k比小于等于k的数量少1，也满足k为中位数

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        diffHash = defaultdict(int)
        diffHash[0] = 1
        greaterK, lessK = 0, 0
        for num in nums:
            greaterK += num > k
            lessK += num <= k
            diffHash[greaterK - lessK] += 1
        ans = 0
        for key, count in diffHash.items():
            if count > 1:
                ans += factorial(count) // factorial(count - 2) // 2
            if key - 1 in diffHash:
                ans += count * diffHash[key - 1]
        return ans


s = Solution()
print(s.countSubarrays(nums=[3, 2, 1, 4, 5], k=4))
print(s.countSubarrays(nums=[2, 3, 1], k=3))

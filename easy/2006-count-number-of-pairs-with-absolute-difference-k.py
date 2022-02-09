'''
2006. 差的绝对值为 K 的数对数目
给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。

|x| 的值定义为：

如果 x >= 0 ，那么值为 x 。
如果 x < 0 ，那么值为 -x 。
 

示例 1：

输入：nums = [1,2,2,1], k = 1
输出：4
解释：差的绝对值为 1 的数对为：
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
示例 2：

输入：nums = [1,3], k = 3
输出：0
解释：没有任何数对差的绝对值为 3 。
示例 3：

输入：nums = [3,2,1,5,4], k = 2
输出：3
解释：差的绝对值为 2 的数对为：
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
'''

from typing import List
'''
思路：计数
将所有的数值用数组counter进行计数，然后再遍历数组counter中每个数值，累计与每个数值差为k的数对个数

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = [0] * 101
        for num in nums:
            counter[num] += 1
        ans = 0
        for num, count in enumerate(counter):
            if count > 0 and num > k and counter[num - k] > 0:
                ans += counter[num - k] * count
        return ans


s = Solution()
print(s.countKDifference(nums=[1, 2, 2, 1], k=1))
print(s.countKDifference(nums=[1, 3], k=3))
print(s.countKDifference(nums=[3, 2, 1, 5, 4], k=2))

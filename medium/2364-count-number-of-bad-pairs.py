'''
2364. 统计坏数对的数目
给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j) 是一个 坏数对 。

请你返回 nums 中 坏数对 的总数目。

 

示例 1：

输入：nums = [4,1,3,3]
输出：5
解释：数对 (0, 1) 是坏数对，因为 1 - 0 != 1 - 4 。
数对 (0, 2) 是坏数对，因为 2 - 0 != 3 - 4, 2 != -1 。
数对 (0, 3) 是坏数对，因为 3 - 0 != 3 - 4, 3 != -1 。
数对 (1, 2) 是坏数对，因为 2 - 1 != 3 - 1, 1 != 2 。
数对 (2, 3) 是坏数对，因为 3 - 2 != 3 - 3, 1 != 0 。
总共有 5 个坏数对，所以我们返回 5 。
示例 2：

输入：nums = [1,2,3,4,5]
输出：0
解释：没有坏数对。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''
from typing import Counter, List
'''
思路：哈希 数学
所有数对的个数可以用等差序列求和公式得出，大约是O(n^2)
可以先找出所有的好数对，好数对的判断标准是j - i != nums[j] - nums[i]，也就是j-nums[j]==i-nums[i]。
遍历一次nums，将i-nums[i]加入哈希表进行计数，具有相同key值的，可以构成好数对（数对个数同样用等差序列求和公式计算）。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = Counter(i - v for i, v in enumerate(nums))  # 统计所有的i-nums[i]
        goodPairs = sum((cnt * (cnt - 1)) >> 1 for cnt in counter.values())  # 计算好数对个数
        return ((len(nums) * (len(nums) - 1)) >> 1) - goodPairs  # 所有数对个数-好数对个数

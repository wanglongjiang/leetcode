'''
面试题 16.24. 数对和
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。

示例 1:

输入: nums = [5,6,5], target = 11
输出: [[5,6]]
示例 2:

输入: nums = [5,6,5,6], target = 11
输出: [[5,6],[5,6]]
提示：

nums.length <= 100000
'''
from typing import List
from collections import Counter
'''
思路：哈希
首先，遍历nums，对所有整数进行计数，保存到counter中；
然后，再次遍历nums，对于每个数字nums[i]，在counter中查找target-nums[i]，
> 如果能找到且其个数>0，将这一对数加入结果，并将2个数在counter中减一
> 如果找不到，跳过当前数字。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        counter = Counter(nums)
        ans = []
        for num in nums:
            if counter[num] == 0:
                continue
            counter[num] -= 1
            other = target - num
            if counter[other] > 0:
                ans.append([num, other])
                counter[other] -= 1
        return ans


s = Solution()
print(s.pairSums([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 12))
print(s.pairSums(nums=[5, 6, 5], target=11))
print(s.pairSums(nums=[5, 6, 5, 6], target=11))

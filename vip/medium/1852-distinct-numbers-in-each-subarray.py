'''
1852. 每个子数组的数字种类数
给你一个整数数组 nums与一个整数 k，请你构造一个长度 n-k+1 的数组 ans，这个数组第i个元素 ans[i] 是每个长度为k的子数组 nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]]
中数字的种类数。

返回这个数组 ans。

示例 1:

输入: nums = [1,2,3,2,2,1,3], k = 3
输出: [3,2,2,2,3]
解释：每个子数组的数字种类计算方法如下：
- nums[0:2] = [1,2,3] 有'1','2','3'三种数字所以      ans[0] = 3
- nums[1:3] = [2,3,2] 有'2','3'两种数字所以          ans[1] = 2
- nums[2:4] = [3,2,2] 有'2','3'两种数字所以          ans[2] = 2
- nums[3:5] = [2,2,1] 有'1','2'两种数字所以          ans[3] = 2
- nums[4:6] = [2,1,3] 有'1','2','3'三种数字所以      ans[4] = 3
示例 2:

输入: nums = [1,1,1,1,2,3,4], k = 4
输出: [1,2,3,4]
解释: 每个子数组的数字种类计算方法如下：
- nums[0:3] = [1,1,1,1] 只有'1'这一种数字所以         ans[0] = 1
- nums[1:4] = [1,1,1,2] 有'1','2'两种数字所以         ans[1] = 2
- nums[2:5] = [1,1,2,3] 有'1','2','3'三种数字所以     ans[2] = 3
- nums[3:6] = [1,2,3,4] 有'1','2','3','4'四种数字所以 ans[3] = 4


提示:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''
from typing import List
from collections import defaultdict
'''
思路：滑动窗口 计数
设一个大小为k的滑动窗口，窗口内的元素保存到哈希表中。
滑动窗口每移动一步，在哈希表中移出一个元素，移入一个元素，并将此时的哈希表中key的数量保存到结果中

时间复杂度：O(n)，数组遍历一次
空间复杂度：O(k)，哈希表的大小为k
'''


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        counter = defaultdict(int)
        for num in nums[:k]:  # 添加前k个元素
            counter[num] += 1
        ans[0] = len(counter)
        for i in range(k, n):
            counter[nums[i - k]] -= 1
            counter[nums[i]] += 1
            if counter[nums[i - k]] == 0:
                del counter[nums[i - k]]
            ans[i - k + 1] = len(counter)
        return ans


s = Solution()
print(s.distinctNumbers(nums=[1, 1, 1, 1, 2, 3, 4], k=4))
print(s.distinctNumbers(nums=[1, 2, 3, 2, 2, 1, 3], k=3))

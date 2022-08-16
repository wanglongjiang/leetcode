'''
2348. 全 0 子数组的数目
给你一个整数数组 nums ，返回全部为 0 的 子数组 数目。

子数组 是一个数组中一段连续非空元素组成的序列。

 

示例 1：

输入：nums = [1,3,0,0,2,0,0,4]
输出：6
解释：
子数组 [0] 出现了 4 次。
子数组 [0,0] 出现了 2 次。
不存在长度大于 2 的全 0 子数组，所以我们返回 6 。
示例 2：

输入：nums = [0,0,0,2,0,0]
输出：9
解释：
子数组 [0] 出现了 5 次。
子数组 [0,0] 出现了 3 次。
子数组 [0,0,0] 出现了 1 次。
不存在长度大于 3 的全 0 子数组，所以我们返回 9 。
示例 3：

输入：nums = [2,10,2019]
输出：0
解释：没有全 0 子数组，所以我们返回 0 。
 

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
from typing import List
'''
思路：双指针
用双指针找到所有连续全是0的子数组，每个连续子数组中的0子数组个数可以用等差公式算出

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, right, n = 0, 0, len(nums)
        ans = 0
        while right < n:
            while right < n and nums[right]:  # 跳过非0元素
                right += 1
            left = right  # left指针固定到子数组第1个0
            while right < n and nums[right] == 0:  # 跳过0
                right += 1
            if left < n:
                ans += (right - left) * (1 + right - left) // 2  #　等差序列求和公式计算0数组个数
        return ans


s = Solution()
print(s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
print(s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
print(s.zeroFilledSubarray([2, 10, 2019]))

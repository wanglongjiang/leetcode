'''
最高频元素的频数
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。

 

示例 1：

输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
示例 2：

输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
示例 3：

输入：nums = [3,9,6], k = 2
输出：1
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序+滑动窗口
较小的数是坑，实际上是将k分拆，填平这些较小的数，使其与子数组最大的数相同。
那么如果想要子数组最长，就要将接近的数排在一起，可以通过排序解决。
然后需要用k来填补较小的数字形成的洼地，可以用滑动窗口解决：
left,right指针分别指向滑动窗口的两端，设滑动窗口内的和=total，滑动窗口最大值*窗口大小=product为理想的和
设diff=product-total，
> 如果diff<=k，那么k能填充较小的数形成的洼地，需要向右移动right指针，扩大窗口大小；
> 如果diff>k，k无法填充形成的洼地，需要向右移动left指针，缩小窗口大小；
重复以上过程，过程中积累最大的窗口大小。

时间复杂度：O(nlogn)，排序需要O(nlogn)，滑动窗口需要O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, n = 0, 0, len(nums)
        total = 0
        ans = 0
        while right < n:
            if (right - left + 1) * nums[right] - (total + nums[right]) <= k:
                total += nums[right]
                right += 1
                ans = max(ans, right - left)
            else:
                total -= nums[left]
                left += 1
        return ans


s = Solution()
print(s.maxFrequency([2, 3, 4], k=2))
print(s.maxFrequency(nums=[1, 2, 4], k=5))
print(s.maxFrequency(nums=[1, 4, 8, 13], k=5))
print(s.maxFrequency(nums=[3, 9, 6], k=2))

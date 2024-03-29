'''
2134. 最少交换次数来组合所有的 1 II
交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。

环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。

给你一个 二进制环形 数组 nums ，返回在 任意位置 将数组中的所有 1 聚集在一起需要的最少交换次数。

 

示例 1：

输入：nums = [0,1,0,1,1,0,0]
输出：1
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[0,0,1,1,1,0,0] 交换 1 次。
[0,1,1,1,0,0,0] 交换 1 次。
[1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 1 。
示例 2：

输入：nums = [0,1,1,1,0,0,1,1,0]
输出：2
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
[1,1,1,1,1,0,0,0,0] 交换 2 次。
无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 2 。
示例 3：

输入：nums = [1,1,0,0,1]
输出：0
解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
因此，需要的最少交换次数为 0 。
 

提示：

1 <= nums.length <= 10^5
nums[i] 为 0 或者 1
'''

from typing import List
'''
思路：滑动窗口
首先统计数组中1的个数width。
然后设一个大小为width的滑动窗口，滑动窗口依次滑过数组，窗口中0的个数即为当前窗口想要变成全是1的子数组需要交换次数。当滑动窗口遍历完整个数组后，就能统计出最小交换次数

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        counter = [0, 0]
        n = len(nums)
        for num in nums:
            counter[num] += 1
        width = counter[1]
        if width <= 1 or n - width <= 1:  # 特殊处理，如果窗口宽度小于等于1，不需要处理，所有的1紧邻；如果0的个数小于等于0，不需要处理，所有的1紧邻
            return 0
        count = 0
        for i in range(width):  # 统计第1个窗口的1的个数
            count += nums[i]
        if count == width:
            return 0
        ans = width - count
        for i in range(width, n + width):  # 滑动窗口， 窗口中0的个数即为需要交换的个数
            count -= nums[i - width]
            count += nums[i % n]
            ans = min(ans, width - count)
            if ans == 0:
                return 0
        return ans


s = Solution()
print(s.minSwaps([0, 1, 0, 1, 1, 0, 0]))
print(s.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))
print(s.minSwaps([1, 1, 0, 0, 1]))

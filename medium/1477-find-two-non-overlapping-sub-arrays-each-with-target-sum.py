'''
1477. 找两个和为目标值且不重叠的子数组
给你一个整数数组 arr 和一个整数值 target 。

请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

 

示例 1：

输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：

输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，
因为它们的长度和 2 是最小值。
示例 3：

输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。
示例 4：

输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。
示例 5：

输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
'''
from typing import List
'''
思路：滑动窗口 后缀数组
1、先用滑动窗口将所有的和为target的子数组找到，子数组开始、结束索引保存到数组starts，ends中。
2、从右向左遍历一次starts,ends，将截止当前索引i的最小子数组长度保存起来，保存到后缀数组minlen中
3、从左向右遍历starts,ends，针对每个子数组i，找到与其不相交的右边最近的子数组j，与其不相交的最小子数组和即为ends[i]-starts[i]+minlen[j]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        starts, ends = [], []
        left, right, n = 0, 0, len(arr)
        s = 0
        # 滑动窗口查找所有的子数组
        while right < n:
            while right < n and s < target:
                s += arr[right]
                right += 1
            if s == target:
                starts.append(left)
                ends.append(right)
                s -= arr[left]
                left += 1
            while left < right and s > target:
                s -= arr[left]
                left += 1
        if not starts:
            return -1
        # 查找最小数组后缀数组
        minlen = [0] * len(starts)
        minlen[-1] = ends[-1] - starts[-1]
        for i in range(len(starts) - 2, -1, -1):
            minlen[i] = min(ends[i] - starts[i], minlen[i + 1])
        # 找到每个子数组与其右边不相交子数组的最小长度和
        right, ans = 0, -1
        for i in range(len(starts)):
            while right < len(starts) and ends[i] > starts[right]:
                right += 1
            if right < len(starts):  # 找到不相交子数组
                ans = ends[i] - starts[i] + minlen[right] if ans == -1 else min(ans, ends[i] - starts[i] + minlen[right])
        return ans


s = Solution()
print(s.minSumOfLengths([7, 3, 4, 7], 7) == 2)  # TODO
print(s.minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))
print(s.minSumOfLengths(arr=[7, 3, 4, 7], target=7))
print(s.minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))
print(s.minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3))
print(s.minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3))

'''
绝对差值和
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。

|x| 定义为：

如果 x >= 0 ，值为 x ，或者
如果 x <= 0 ，值为 -x
 

示例 1：

输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
示例 2：

输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
示例 3：

输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

提示：

n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-sum-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import bisect
'''
思路：二分查找 贪心
1. 对nums1的copy进行排序
2. 遍历nums1、nums2，累计其绝对值差和，然后在nums1copy中查找与nums2[i]最接近的数值a，记住最大的abs(nums1[i]-a)
3. 将绝对值差和减掉上面第2步求出的最大abs(nums1[i]-a)得到结果

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sortedNums1, n = list(sorted(nums1)), len(nums1)
        ans, maxDiff = 0, float('-inf')
        for n1, n2 in zip(nums1, nums2):
            ans += abs(n1 - n2)
            i = bisect.bisect_left(sortedNums1, n2)  # 在nums1中查找接近n2的索引
            a = 0  # 下面2个判断用于查找最接近n2的数值a
            if i < n:
                a = sortedNums1[i]
            if i > 0 and abs(sortedNums1[i - 1] - n2) < abs(a - n2):
                a = sortedNums1[i - 1]
            maxDiff = max(maxDiff, abs(abs(a - n2) - abs(n1 - n2)))  # 用贪心策略找到用a替换nums1[i]之后收益最大的
        return (ans - maxDiff) % (10**9 + 7)


s = Solution()
print(s.minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
print(s.minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
print(s.minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))

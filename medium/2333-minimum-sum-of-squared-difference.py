'''
2333. 最小差值平方和
给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度为 n 。

数组 nums1 和 nums2 的 差值平方和 定义为所有满足 0 <= i < n 的 (nums1[i] - nums2[i])2 之和。

同时给你两个正整数 k1 和 k2 。你可以将 nums1 中的任意元素 +1 或者 -1 至多 k1 次。类似的，你可以将 nums2 中的任意元素 +1 或者 -1 至多 k2 次。

请你返回修改数组 nums1 至多 k1 次且修改数组 nums2 至多 k2 次后的最小 差值平方和 。

注意：你可以将数组中的元素变成 负 整数。

 

示例 1：

输入：nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
输出：579
解释：nums1 和 nums2 中的元素不能修改，因为 k1 = 0 和 k2 = 0 。
差值平方和为：(1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579 。
示例 2：

输入：nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
输出：43
解释：一种得到最小差值平方和的方式为：
- 将 nums1[0] 增加一次。
- 将 nums2[2] 增加一次。
最小差值平方和为：
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43 。
注意，也有其他方式可以得到最小差值平方和，但没有得到比 43 更小答案的方案。
 

提示：

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[i] <= 105
0 <= k1, k2 <= 109
'''

from typing import List
'''
思路：排序
计算2个数组的差值，按照从大到小进行排序
依次将最大值减一
TODO
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = list(sorted(map(lambda p: abs(p[0] - p[1]), zip(nums1, nums2)), reverse=True))
        k, n = k1 + k2, len(diffs)
        for i in range(1, n):
            if k > 0:
                if i * (diffs[i - 1] - diffs[i]) > k:
                    k -= i * (diffs[i - 1] - diffs[i])
                else:
                    return
        return 0

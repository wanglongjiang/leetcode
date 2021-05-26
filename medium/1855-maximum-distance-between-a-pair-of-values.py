'''
下标对中的最大距离

给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。

下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且 nums1[i] <= nums2[j] ，
则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​

返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。

一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。

 

示例 1：
输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
输出：2
解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
最大距离是 2 ，对应下标对 (2,4) 。

示例 2：
输入：nums1 = [2,2,2], nums2 = [10,10,1]
输出：1
解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
最大距离是 1 ，对应下标对 (0,1) 。

示例 3：
输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
输出：2
解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
最大距离是 2 ，对应下标对 (2,4) 。

示例 4：
输入：nums1 = [5,4], nums2 = [3,2]
输出：0
解释：不存在有效下标对，所以返回 0 。
 

提示：

1 <= nums1.length <= 10^5
1 <= nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^5
nums1 和 nums2 都是 非递增 数组
'''
from typing import List
'''
思路：双指针
初始最大距离ans = 0
设2个指针p1,p2分别指向nums1的末尾，nums2的末尾
1. 然后设p1=min(p2-ans,p1)，开始对比p1,p2指向的元素大小，如果满足nums2[p2]>=nums1[p1]，则p1向左移动，直至不满足条件，设最大距离为ans
2. 再将p2向左移动，此时如果有更大距离，必然p1也要向左移动一位，所以重复上面过程1，直至nums1遍历完成


时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        p2 = len(nums2) - 1
        p1 = min(len(nums1) - 1, p2)
        while p1 >= 0:
            while p1 >= 0 and nums2[p2] >= nums1[p1]:
                ans = max(ans, p2 - p1)
                p1 -= 1
            p2 -= 1
            p1 = min(p2 - ans, p1)
        return ans


s = Solution()
print(s.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
print(s.maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]))
print(s.maxDistance(nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]))
print(s.maxDistance(nums1=[5, 4], nums2=[3, 2]))

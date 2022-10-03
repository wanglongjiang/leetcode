'''
2425. 所有数对的异或和
给你两个下标从 0 开始的数组 nums1 和 nums2 ，两个数组都只包含非负整数。请你求出另外一个数组 nums3 ，
包含 nums1 和 nums2 中 所有数对 的异或和（nums1 中每个整数都跟 nums2 中每个整数 恰好 匹配一次）。

请你返回 nums3 中所有整数的 异或和 。

 

示例 1：

输入：nums1 = [2,1,3], nums2 = [10,2,5,0]
输出：13
解释：
一个可能的 nums3 数组是 [8,0,7,2,11,3,4,1,9,1,6,3] 。
所有这些数字的异或和是 13 ，所以我们返回 13 。
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：0
解释：
所有数对异或和的结果分别为 nums1[0] ^ nums2[0] ，nums1[0] ^ nums2[1] ，nums1[1] ^ nums2[0] 和 nums1[1] ^ nums2[1] 。
所以，一个可能的 nums3 数组是 [2,5,1,6] 。
2 ^ 5 ^ 1 ^ 6 = 0 ，所以我们返回 0 。
 

提示：

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
'''
import functools
import operator
from typing import List
'''
思路：位运算
从题目中得知nums1[i]需要参与异或的运算是nums1[i]^nums2[0]..nums1[i]^nums2[n-1]
nums1[i]参与异或运算的次数取决于nums2的长度，如果是偶数次，那么为0；如果是奇数次，那么为nums1[i]。
nums2[i]与nums1[i]同理，其参与异或运算的次数取决于nums1的长度。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1xor = 0 if len(nums2) % 2 == 0 else functools.reduce(operator.xor, nums1)
        n2xor = 0 if len(nums1) % 2 == 0 else functools.reduce(operator.xor, nums2)
        return n1xor ^ n2xor


s = Solution()
assert s.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]) == 13

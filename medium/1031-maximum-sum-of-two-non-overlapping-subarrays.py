'''
1031. 两个非重叠子数组的最大和
给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。
（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）

从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) 并满足下列条件之一：

 

0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

示例 1：

输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
示例 2：

输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
示例 3：

输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
 

提示：

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
'''
from typing import List
'''
思路：滑动窗口
首先用滑动窗口从左向右扫描所有长度为firstlen的子数组的和，并用一个前缀数组保存截止每个下标的最大子数组和。
然后用滑动窗口从右向左扫描所有长度为firstlen的子数组的和，并用一个后缀数组保存截止每个下标的最大子数组和。
最后用滑动窗口从左向右扫描所有长度为secondlen的子数组和，其分别与前缀组数、后缀数组中最大子数组的和选择最大的那个。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix, postfix = [0] * n, [0] * n
        # 计算前缀最大子数组和
        s = sum(nums[:firstLen])
        prefix[firstLen - 1] = s
        for i in range(firstLen, n):
            s += nums[i] - nums[i - firstLen]
            prefix[i] = max(prefix[i - 1], s)
        # 计算后缀最大子数组和
        s = sum(nums[-firstLen:])
        postfix[-firstLen] = s
        for i in range(n - firstLen - 1, -1, -1):
            s += nums[i] - nums[i + firstLen]
            postfix[i] = max(postfix[i + 1], s)
        # 找到最大的子数组和
        s = sum(nums[:secondLen])
        ans = max(s + postfix[secondLen], sum(nums[-secondLen:]) + prefix[n - secondLen - 1])
        for i in range(secondLen, n - 1):
            s += nums[i] - nums[i - secondLen]
            ans = max(ans, prefix[i - secondLen] + s, postfix[i + 1] + s)
        return ans


s = Solution()
print(s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
print(s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
print(s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))

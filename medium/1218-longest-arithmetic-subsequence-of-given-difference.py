'''
最长定差子序列
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

 

示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
 

提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4
'''
from typing import List
'''
思路：哈希
从左到右遍历数组，对于当前元素arr[i]，判断在哈希表中是否存在prev == arr[i]-difference
如果存在，则将hash[arr[i]]设置为hash[prev]+1
如果不存在，将hash[arr[i]]设置为1
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        dp = {}
        for num in arr:
            prev = num - difference
            if prev in dp:
                dp[num] = dp[prev] + 1
                if dp[num] > ans:
                    ans = dp[num]
            else:
                dp[num] = 1
        return ans


s = Solution()
print(s.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
print(s.longestSubsequence(arr=[1, 3, 5, 7], difference=1))
print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))

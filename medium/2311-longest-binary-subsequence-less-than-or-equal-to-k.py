'''
2311. 小于等于 K 的最长二进制子序列
给你一个二进制字符串 s 和一个正整数 k 。

请你返回 s 的 最长 子序列，且该子序列对应的 二进制 数字小于等于 k 。

注意：

子序列可以有 前导 0 。
空字符串视为 0 。
子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
 

示例 1：

输入：s = "1001010", k = 5
输出：5
解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
最长子序列的长度为 5 ，所以返回 5 。
示例 2：

输入：s = "00101001", k = 1
输出：6
解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
最长子序列的长度为 6 ，所以返回 6 。
 

提示：

1 <= s.length <= 1000
s[i] 要么是 '0' ，要么是 '1' 。
1 <= k <= 109
'''
'''
思路：滑动窗口
设k的二进制字符串长度为m，设置一个长度为m的滑动窗口，滑过s，
如果窗口内的数值小于等于k，此时最长子序列长度为s[0..i]中1的数量+m
如果窗口内的数值大于k，那么减去最高位的1之后，其值小于k，此时最长子序列长度为s[0..i]中1的数量+m-1

时间复杂度：O(nm),m=log(k),n=len(s)
空间复杂度：O(m)
'''


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        strk = bin(k)[2:]
        m, n = len(strk), len(s)
        ans = 0

        def kGtOrEq(start):
            for i in range(start, start + m):
                if s[i] == strk[i - start]:
                    continue
                if s[i] == '0':
                    return True
                else:
                    return False
            return True

        zeroCount = 0
        for i in range(n - m + 1):
            if kGtOrEq(i):
                ans = max(ans, m + zeroCount)
            else:
                ans = max(ans, m + zeroCount - 1)
            if s[i] == '0':
                zeroCount += 1
        return ans


s = Solution()
print(s.longestSubsequence(s="1", k=1))
print(s.longestSubsequence(s="01", k=1))
print(s.longestSubsequence(s="00101001", k=1))
print(s.longestSubsequence(s="1001010", k=5))

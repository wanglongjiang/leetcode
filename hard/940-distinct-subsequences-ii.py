'''
940. 不同的子序列 II
给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。

字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。
 

示例 1：

输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
示例 2：

输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
示例 3：

输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
 

提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成
'''
'''
动态规划

根据题意我们设dp[i]为前i个字符可以组成的不同的子序列，则有

dp[i] = dp[i - 1] + newCount - repeatCount

d[i] 和 d[i-1] 之间有什么关系？

dp[i] = dp[i - 1] + newCount - repeatCount

newCount 如何计算？

子集个数为2^n，所以 newCount = dp[i-1]

repeatCount如何计算？

以字符串“abcb”为例，dp[2] - dp[1] 是引入第一个'b'新增的子串个数，那么当引入第二个‘b’的时候重复子串个数也为 dp[2] - dp[1]

'''


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        m, n = 10**9 + 7, len(s)
        preCount = [0] * 26
        curAns = 1
        for i in range(n):
            newCount = curAns
            curAns = ((curAns + newCount) % m - preCount[ord(s[i]) - ord('a')] % m + m) % m
            preCount[ord(s[i]) - ord('a')] = newCount
        return curAns - 1

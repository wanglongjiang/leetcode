'''
467. 环绕字符串中唯一的子字符串
把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." . 
现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。 

 

示例 1:

输入: p = "a"
输出: 1
解释: 字符串 s 中只有一个"a"子字符。
示例 2:

输入: p = "cac"
输出: 2
解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.
示例 3:

输入: p = "zab"
输出: 6
解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
 

提示:

1 <= p.length <= 105
p 由小写英文字母构成
'''

from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())

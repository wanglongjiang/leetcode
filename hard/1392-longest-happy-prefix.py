'''
最长快乐前缀
「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。

给你一个字符串 s，请你返回它的 最长快乐前缀。

如果不存在满足题意的前缀，则返回一个空字符串。

 

示例 1：

输入：s = "level"
输出："l"
解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。
最长的既是前缀也是后缀的字符串是 "l" 。
示例 2：

输入：s = "ababab"
输出："abab"
解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
示例 3：

输入：s = "leetcodeleet"
输出："leet"
示例 4：

输入：s = "a"
输出：""
 

提示：

1 <= s.length <= 10^5
s 只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-happy-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：滚动哈希
计算s的所有前缀和所有后缀的哈希，然后对比相同长度的哈希值是否相同

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        b = 100007
        m = 2 ^ 64
        prefixHash = [0] * n
        prefixHash[0] = 0
        for i in range(1, n):
            prefixHash[i] = (prefixHash[i - 1] * b + ord(s[i - 1])) % m  # 计算前缀字符串的哈希
        t = 1
        postfixHash = 0
        start = 0
        for i in range(n - 1, 0, -1):
            postfixHash = (ord(s[i]) * t + postfixHash) % m  # 计算后缀字符串的哈希
            if postfixHash == prefixHash[n - i]:  # 比较相同长度的前缀、后缀的哈希是否相同，如果相同，更新后缀字符串的开始索引
                start = i
            t = (t * b) % m
        if start:
            return s[start:]
        return ''


s = Solution()
print(s.longestPrefix('level'))
print(s.longestPrefix('ababab'))
print(s.longestPrefix('leetcodeleet'))
print(s.longestPrefix('a'))
print(s.longestPrefix('aa'))
print(s.longestPrefix('aaa'))

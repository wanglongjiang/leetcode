'''
统计只差一个字符的子串数目
给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。

比方说， "computer" 和 "computation" 加粗部分只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。

请你返回满足上述条件的不同子字符串对数目。

一个 子字符串 是一个字符串中连续的字符。

 

示例 1：

输入：s = "aba", t = "baba"
输出：6
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 2：
输入：s = "ab", t = "bb"
输出：3
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("ab", "bb")
("ab", "bb")
("ab", "bb")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 3：
输入：s = "a", t = "a"
输出：0

示例 4：
输入：s = "abe", t = "bbc"
输出：10
 

提示：

1 <= s.length, t.length <= 100
s 和 t 都只包含小写英文字母。
'''
'''
思路：回文串思路
利用类似于回文串的思路，先找到2个字符串中任意2个不同的字符，然后从这个字符出发，向2个方向遍历相同的字符。
设s[i]与t[j]不同，s[i-left..i-1]与t[j-left..j-1]为相同字符，s[i+1..i+right]与t[j+1..j+right]为相同字符
那么这个区间的子字符串都符合题意，他们的组合数量为left*right。
根据上面的思路写出代码。

时间复杂度：O(mn*min(m,n))
空间复杂度：O(1)
'''


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:  # 找到一个不同的字符
                    left = 1
                    while i - left >= 0 and j - left >= 0 and s[i - left] == t[j - left]:  # 向左扩大相同字符串范围
                        left += 1
                    right = 1
                    while i + right < m and j + right < n and s[i + right] == t[j + right]:  # 向右扩大相同字符串范围
                        right += 1
                    ans += left * right
        return ans


s = Solution()
print(s.countSubstrings(s="aba", t="baba"))
print(s.countSubstrings(s="ab", t="bb"))
print(s.countSubstrings(s="a", t="a"))
print(s.countSubstrings(s="abe", t="bbc"))

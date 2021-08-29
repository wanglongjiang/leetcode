'''
1180. 统计只含单一字母的子串
给你一个字符串 S，返回只含 单一字母 的子串个数。

示例 1：

输入： "aaaba"
输出： 8
解释：
只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。
示例 2:

输入： "aaaaaaaaaa"
输出： 55


提示：

1 <= S.length <= 1000
S[i] 仅由小写英文字母组成。
'''
'''
思路：数学
遍历字符串，计算每个连续字符串的长度
长度为n的连续字符串可以构成n*(n+1)/2个子字符串

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        preChar, count = '', 0
        for char in s:
            if preChar != char:
                ans += count * (count + 1) // 2
                preChar = char
                count = 1
            else:
                count += 1
        return ans + count * (count + 1) // 2


s = Solution()
print(s.countLetters('aaaba'))
print(s.countLetters('aaaaaaaaaa'))

'''
定长子串中元音的最大数目
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。

 

示例 1：
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。

示例 2：
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。

示例 3：
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

示例 4：
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。

示例 5：
输入：s = "tryhard", k = 4
输出：1
 

提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length
'''
'''
思路：滑动窗口
典型的滑动窗口问题，从左到右滑动窗口，滑入的字符是元音+1，滑出的字符是元音-1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        ans = 0
        n = len(s)
        for i in range(k):  # 记录最开始的窗口元音数
            if s[i] in vowels:
                ans += 1
        cnt = ans
        for i in range(k, n):  # 滑动窗口
            if s[i] in vowels:  # 增加移入的元音
                cnt += 1
            if s[i - k] in vowels:  # 减少移出的元音
                cnt -= 1
            if cnt > ans:
                ans = cnt
        return ans


s = Solution()
print(s.maxVowels(s="abciiidef", k=3))
print(s.maxVowels(s="aeiou", k=2))
print(s.maxVowels(s="leetcode", k=3))
print(s.maxVowels(s="rhythms", k=4))
print(s.maxVowels(s="tryhard", k=4))

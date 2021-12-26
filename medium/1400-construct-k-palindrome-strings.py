'''
1400. 构造 K 个回文字符串
给你一个字符串 s 和一个整数 k 。请你用 s 字符串中 所有字符 构造 k 个非空 回文串 。

如果你可以用 s 中所有字符构造 k 个回文字符串，那么请你返回 True ，否则返回 False 。



示例 1：

输入：s = "annabelle", k = 2
输出：true
解释：可以用 s 中所有字符构造 2 个回文字符串。
一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"
示例 2：

输入：s = "leetcode", k = 3
输出：false
解释：无法用 s 中所有字符构造 3 个回文串。
示例 3：

输入：s = "true", k = 4
输出：true
解释：唯一可行的方案是让 s 中每个字符单独构成一个字符串。
示例 4：

输入：s = "yzyzyzyzyzyzyzy", k = 2
输出：true
解释：你只需要将所有的 z 放在一个字符串中，所有的 y 放在另一个字符串中。那么两个字符串都是回文串。
示例 5：

输入：s = "cr", k = 7
输出：false
解释：我们没有足够的字符去构造 7 个回文串。


提示：

1 <= s.length <= 10^5
s 中所有字符都是小写英文字母。
1 <= k <= 10^5
'''
from collections import Counter
'''
思路：计数 贪心
要分成k个回文串，总的字符数要大于k；
字符的个数为奇数的，要小于等于k，也就是每个回文串里面最多有1个个数为奇数的字符，可以用计数对所有字符个数进行统计

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        odd = 0
        for char, v in counter.items():
            if v % 2:
                odd += 1
        if odd > k:
            return False
        return True


s = Solution()
print(s.canConstruct(s="annabelle", k=2))

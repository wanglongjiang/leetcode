'''
266. 回文排列
给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

示例 1：

输入: "code"
输出: false
示例 2：

输入: "aab"
输出: true
示例 3：

输入: "carerac"
输出: true
'''
from collections import Counter
'''
思路：计数
如果字符串长度为偶数，每个字符的个数都是偶数
如果字符串长度为奇数，只允许1个字符的个数是奇数，其他字符都是偶数

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        even = len(s) % 2 == 0
        for char, count in counter.items():
            if count % 2:
                if even:
                    return False
                else:
                    even = True
        return True


s = Solution()
print(s.canPermutePalindrome('code'))
print(s.canPermutePalindrome('carerac'))
print(s.canPermutePalindrome('aab'))

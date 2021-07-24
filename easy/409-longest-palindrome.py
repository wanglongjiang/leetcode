'''
最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict
'''
思路：计数
构成回文串的字符，偶数个数的字符可以任意添加，奇数个数的字符，可以将超过1的加上。
所以，可以对字符串种的所有字符进行奇数。
最长回文串长度为所有的奇数字符+最多的偶数字符

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        ans, maxOdd = 0, 0
        for c, count in counter.items():
            if count % 2:
                if count > 2:
                    ans += count - 1
                maxOdd = 1
            else:
                ans += count
        return ans + maxOdd

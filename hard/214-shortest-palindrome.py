'''
最短回文串
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1：
输入：s = "aacecaaa"
输出："aaacecaaa"


示例 2：
输入：s = "abcd"
输出："dcbabcd"

提示：
0 <= s.length <= 5 * 10^4
s 仅由小写英文字母组成
'''
'''
思路1，中间开始暴力查找法。从字符串的中间字符mid开始，检查mid 两侧的mid个字符串是否对称，如果对称，mid*2..end之间的字符串填充到左边即为回文串。如果不对称，mid指针向左移动，直至对称为止。
时间复杂度：O(n^2)，结合输入5*10^4来看，能达到10^8。
思路2，两侧开始暴力查找法。维护2个左边，left、right，left在最左边，right在最右边，2指针向内收敛，如果字符串一直相同直到2个指针在中间相遇，则right右侧的字符串填充到left左侧即为回文。
    如果2个指针无法相遇，则将right指针向内移动一位，left恢复为0，继续搜索。
时间复杂度：O(n^2)，与上面思路1的时间复杂度相同。
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        while n > 0:
            left, right = 0, n - 1
            while s[left] != s[right]:  # right向内移动到第1个相同字符处
                right -= 1
            n = right  # 下次可以从right所在的位置开始搜索
            while left < right and s[left] == s[right]:  # 向内搜索，直至2个指针相遇或者字符不再相同
                left += 1
                right -= 1
            if left >= right:  # 两个指针相遇，可以将n右边的字符拼接到最左边，返回结果
                i, n = n + 1, len(s)
                s1 = ''
                while i < n:
                    s1 = s[i] + s1
                    i += 1
                return s1 + s
        return s


s = Solution()
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("abcd"))

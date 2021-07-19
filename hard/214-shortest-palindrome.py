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

思路3，滚动哈希
根据题意，如果想要达到最短回文字符串，那么s[0..i..2i]构成的回文串越长越好。
1. 查找从s[0]开始的最长回文串可以使用滚动哈希算法。计算s[0..i]和s[i+1..2i]的哈希，如果哈希相同，则为回文串
2. 那么返回的结果是将s[2i+1..n-1]逆序后，拼接到s前面

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路3，滚动哈希
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        b = 10007  # 哈希的基数
        beforeHash, afterHash = 0, 0
        t = 1  # 累计b的n/2次方
        for i in range(n // 2):
            beforeHash = beforeHash * b + ord(s[i])  # 从前向后计算前半部分的哈希
            afterHash = afterHash * b + ord(s[n - i - 1])  # 从后往前计算后半部分的哈希
            t *= b
        t //= b
        for j in range(n - 1, 0, -1):
            if beforeHash == afterHash:  # 哈希值相同，找到回文
                break
            if j % 2:  # 子串长度为偶数，需要将前半部缩小1个字符，后半部缩小1个字符
                i = j // 2  # 得到前半部分的最后一个坐标
                beforeHash = (beforeHash - ord(s[i])) // b
                afterHash = afterHash - ord(s[j]) * t
                t //= b
            else:  # 子串长度为奇数，需要将后半部分向前移动一个字符
                i = j // 2  # 得到中间字符的索引，后半部分的索引需要加上它
                afterHash = (afterHash - ord(s[j]) * t) * b + ord(s[i])
        else:  # 未找到回文，将第1个字符后面的子串反序后连结
            return s[1:][::-1] + s
        return s[j + 1:][::-1] + s  # 找到回文，将回文后面的字符串反序后连结s

    # 思路2，暴力查找
    def shortestPalindrome2(self, s: str) -> str:
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
print(s.shortestPalindrome("abcddcbae"))
print(s.shortestPalindrome("aaaaaee"))
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("abcd"))

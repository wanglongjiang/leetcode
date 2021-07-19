'''
面试题 01.06. 字符串压缩
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。
若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。
'''
'''
思路：数组
遍历字符串，将重复字符进行计数，字符和个数保存到数组

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        i = 0
        ans = []
        anslen = 0
        while i < n and anslen < n:
            char = S[i]
            count = 0
            while i < n and char == S[i]:
                count += 1
                i += 1
            ans.append(char)
            ans.append(str(count))
            anslen += 1 + len(ans[-1])
        if anslen >= n:
            return S
        return ''.join(ans)


s = Solution()
print(s.compressString('aabcccccaaa'))

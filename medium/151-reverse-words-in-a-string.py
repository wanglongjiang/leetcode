'''
翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

进阶：

请尝试使用 O(1) 额外空间复杂度的原地解法。
'''
'''
思路：栈。python和java里面的字符串都是不可变对象，没法做到O(1)，用栈吧。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        left, right = 0, 0
        n = len(s)
        while right < n:
            while right < n and s[right] == ' ':
                right += 1
            if right < n:
                left = right
                while right < n and s[right] != ' ':
                    right += 1
                stack.append(s[left:right])
        stack.reverse()
        return ' '.join(stack)


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world!  "))
print(s.reverseWords("a good   example"))
print(s.reverseWords("  Bob    Loves  Alice   "))
print(s.reverseWords("Alice does not even like bob"))

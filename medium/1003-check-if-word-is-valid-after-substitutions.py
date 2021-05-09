'''
检查替换后的词是否有效
给你一个字符串 s ，请你判断它是否 有效 。
字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：

将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。
注意，tleft 和 tright 可能为 空 。
如果字符串 s 有效，则返回 true；否则，返回 false。

 

示例 1：

输入：s = "aabcbc"
输出：true
解释：
"" -> "abc" -> "aabcbc"
因此，"aabcbc" 有效。
示例 2：

输入：s = "abcabcababcc"
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。
示例 3：

输入：s = "abccba"
输出：false
解释：执行操作无法得到 "abccba" 。
示例 4：

输入：s = "cababc"
输出：false
解释：执行操作无法得到 "cababc" 。
 

提示：

1 <= s.length <= 2 * 104
s 由字母 'a'、'b' 和 'c' 组成
'''
'''
思路：栈
遇到'a','b'入栈，遇到'c'需要连续出栈'b''a'，最后栈为空。
如果不满足如上条件，则不是合法字符串
时间复杂度：O(n)，每个字符最多入栈1次
空间复杂度：O(n)，最多所有字符入栈
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == 'a' or c == 'b':
                stack.append(c)
            else:
                if not stack or stack.pop() != 'b':
                    return False
                if not stack or stack.pop() != 'a':
                    return False
        if stack:
            return False
        return True


s = Solution()
print(s.isValid("aabcbc"))
print(s.isValid("abcabcababcc"))
print(s.isValid("abccba"))
print(s.isValid("cababc"))

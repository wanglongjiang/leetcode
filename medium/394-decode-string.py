'''
字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"


示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"


示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"


示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

示例 5：
输入：s = "3[a2[c]b]"
输出："accbaccbaccb"
'''
'''
思路：栈
遍历输入，遇到数值入栈
遇到字母，查看栈顶元素，如果栈顶元素是字母，与其相加
    如果栈顶元素不是字母，入栈
遇到']'，出栈2个元素，重复创建字符串，入栈
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def decodeString(self, s: str) -> str:
        i, n = 0, len(s)
        stack = []
        while i < n:
            if s[i].isdigit():
                num = ''
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(int(num))
                i += 1  # 跳过'['
            elif s[i] == ']':
                i += 1
                strs = stack.pop() * stack.pop()
                if stack:
                    if type(stack[-1]) == int:
                        stack.append(strs)
                    else:
                        stack.append(stack.pop() + strs)
                else:
                    stack.append(strs)
            else:  # 字母
                strs = ''
                while i < n and not s[i].isdigit() and s[i] != ']':
                    strs += s[i]
                    i += 1
                if stack:
                    if type(stack[-1]) == int:
                        stack.append(strs)
                    else:
                        stack.append(stack.pop() + strs)
                else:
                    stack.append(strs)
        return stack[0]


s = Solution()
print(s.decodeString("3[a]2[bc]") == "aaabcbc")
print(s.decodeString("3[a2[c]]") == "accaccacc")
print(s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(s.decodeString("abc3[cd]xyz") == 'abccdcdcdxyz')
print(s.decodeString("3[a2[c]b]") == 'accbaccbaccb')

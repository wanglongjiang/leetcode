'''
301. 删除无效的括号
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。



示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]


提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号
'''
'''
思路：回溯
整个字符串可以拆分成若干部分，拆分原则是：如果一段括弧串的右括弧超过了左括弧数量，且再向右边遍历是左括弧，那么这段括弧是相对独立的
它如果想要变成合法的括弧，需要回溯删除多余的右括弧。
最右边的部分有3种可能：合法、左括弧超过右括弧、右括弧超过左括弧。
各个独立部分都需要用回溯变成合法的，最后把各个独立部分变成合法的之后再组合。

时间复杂度：O(2^n)
空间复杂度：O(2^n)
'''


class Solution:
    def removeInvalidParentheses(self, s: str):
        res = []

        def remove(s, ibegin, jbegin, tmp1, tmp2):
            left_p = 0
            right_p = 0
            for i in range(ibegin, len(s)):
                if s[i] == tmp1:
                    left_p += 1
                if s[i] == tmp2:
                    right_p += 1
                if left_p < right_p:
                    for j in range(jbegin, i + 1):
                        if s[j] == tmp2 and (j == jbegin or s[j - 1] != tmp2):
                            remove(s[:j] + s[j + 1:], i, j, tmp1, tmp2)

                    return
            rev = s[::-1]
            if tmp1 == "(":
                remove(rev, 0, 0, ")", "(")
            else:
                res.append(rev)

        remove(s, 0, 0, "(", ")")
        return res


s = Solution()
print(s.removeInvalidParentheses(")()))())))"))
print(s.removeInvalidParentheses("(()("))
print(s.removeInvalidParentheses("()())()"))
print(s.removeInvalidParentheses("()()()))()"))
print(s.removeInvalidParentheses("(a)())()"))
print(s.removeInvalidParentheses(s=")("))

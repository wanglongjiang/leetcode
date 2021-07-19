'''
移除无效的括号
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
 

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
示例 2：

输入：s = "a)b(c)d"
输出："ab(c)d"
示例 3：

输入：s = "))(("
输出：""
解释：空字符串也是有效的
示例 4：

输入：s = "(a(b(c)d)"
输出："a(b(c)d)"
 

提示：

1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：栈
遍历字符串，当前字符c
> 如果是'('，入栈，后续字符持续入栈，直至遇到'('或')'；
> 如果是')'，尝试出栈，直至出栈一个匹配的'('，将'('+字符串+')'合并加入栈；如果栈为空，抛弃当前')'
> 如果是普通字符，入栈
遍历完s所有字符后如果栈不为空，将栈中非'('，加入队列头部

最后将q中的字符连结起来就是结果

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i, n = 0, len(s)
        stack = []
        while i < n:
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                if stack:
                    t = stack.pop()
                    if t == '(':
                        stack.append('()')
                    else:
                        if stack and stack[-1] == '(':
                            stack.pop()
                            stack.append('(' + t + ')')
                        else:
                            stack.append(t)
                i += 1
            else:
                j = i
                while j < n and s[j] != '(' and s[j] != ')':
                    j += 1
                stack.append(s[i:j])
                i = j
            if len(stack) > 2 and stack[-1] != '(' and stack[-2] != '(':  # 合并两个合法的字符串
                t = stack.pop()
                stack.append(stack.pop() + t)
        ans = ''
        for t in stack:
            if t != '(':
                ans += t
        return ans


s = Solution()
print(s.minRemoveToMakeValid('lee(t(c)o)de)'))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("(a(b(c)d)"))

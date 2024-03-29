'''
有效的括号字符串
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True
注意:

字符串大小将在 [1，100] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：栈
遍历字符串s，对于当前字符s[i]
> 如果s[i]=='('，'('入栈
> 如果s[i]=='*'，将*的个数入栈（如果栈顶也是数字，将栈顶元素+1，否则入栈1）
> 如果s[i]==')'，
>> 如果栈顶是'('，栈顶元素出栈
>> 如果栈顶是数字（'*'的个数），那么需要将个数出栈，然后再判断栈顶元素是否为'('，如果是'('出栈
执行完上述过程后，依次将栈中元素出栈：
> 如果元素为数字，star+栈顶元素
> 如果元素为'('，star必须大于0，然后star-1；如果start为0，这个左括号没有匹配，返回false
最后返回True

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '*':
                if not stack or stack[-1] == '(':
                    stack.append(1)
                else:
                    stack[-1] += 1
            else:
                if stack:
                    if stack[-1] == '(':  # 栈顶就是左括号，直接与当前右括号匹配
                        stack.pop()
                    else:
                        if len(stack) == 1:  # 栈中只有1个元素，且其是星号的个数，需要将星号个数减1，使1个星号与右括号匹配
                            stack[-1] -= 1
                            if stack[-1] == 0:
                                stack.pop()
                        else:
                            star = stack.pop()  # 星号个数出栈
                            stack.pop()  # 将左括号出栈
                            if stack and stack[-1] != '(':  # 如果栈顶是星号的个数，需要进行合并
                                stack[-1] += star
                            else:
                                stack.append(star)  # 如果栈为空，或者栈顶是左括号，需要将星号个数入栈
                else:
                    return False  # 没有找到匹配的左括号或者星号
        star = 0
        while stack:
            val = stack.pop()
            if val == '(':
                if star > 0:
                    star -= 1
                else:
                    return False
            else:
                star += val
        return True


s = Solution()
print(s.checkValidString('()'))
print(s.checkValidString('(*)'))
print(s.checkValidString('(*))'))
print(s.checkValidString('**(('))
print(s.checkValidString('**)'))

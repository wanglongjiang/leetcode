'''
删除最外层的括号
有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。

例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。

 

示例 1：

输入：s = "(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
示例 2：

输入：s = "(()())(())(()(()))"
输出："()()()()(())"
解释：
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
示例 3：

输入：s = "()()"
输出：""
解释：
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。
 

提示：

1 <= s.length <= 10^5
s[i] 为 '(' 或 ')'
s 是一个有效括号字符串

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-outermost-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：计数
设置变量count用于累计括号嵌套深度，初始值为0
当count>0，遇到的左括号输出，count+1，遇到右括号输出，count-1
当count=0，遇到左括号不输出，count+1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        ans = ''
        for c in S:
            if count > 0:
                if c == '(':
                    count += 1
                    ans += '('
                else:
                    count -= 1
                    if count > 0:
                        ans += ')'
            else:
                count += 1
        return ans
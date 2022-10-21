'''
1717. 删除子字符串的最大得分
给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。

删除子字符串 "ab" 并得到 x 分。
比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
删除子字符串"ba" 并得到 y 分。
比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
请返回对 s 字符串执行上面操作若干次能得到的最大得分。

 

示例 1：

输入：s = "cdbcbbaaabab", x = 4, y = 5
输出：19
解释：
- 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
- 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
- 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
- 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
总得分为 5 + 4 + 5 + 5 = 19 。
示例 2：

输入：s = "aabbaaxybbaabb", x = 5, y = 4
输出：20
 

提示：

1 <= s.length <= 105
1 <= x, y <= 104
s 只包含小写英文字母。
'''
'''
思路：栈 贪心
消除ab的方法是用一个栈进行辅助，遍历字符串，遇到a或其他字符，入栈。
遇到b，如果栈顶是a，则出栈；否则将b入栈。
同理，消除ba的方法类似于上面。

判断x、y哪个数字大，如果x大，首先消除ab，否则先消除ba

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # 消除所有的ab
        def delab(s):
            stk = []
            for char in s:
                if char == 'b' and stk and stk[-1] == 'a':
                    stk.pop()
                else:
                    stk.append(char)
            return stk

        # 消除所有的ba
        def delba(s):
            stk = []
            for char in s:
                if char == 'a' and stk and stk[-1] == 'b':
                    stk.pop()
                else:
                    stk.append(char)
            return stk

        ans = 0
        if x > y:
            news = delab(s)
            ans += (len(s) - len(news)) // 2 * x
            news2 = delba(news)
            ans += (len(news) - len(news2)) // 2 * y
        else:
            news = delba(s)
            ans += (len(s) - len(news)) // 2 * y
            news2 = delab(news)
            ans += (len(news) - len(news2)) // 2 * x
        return ans


s = Solution()
assert s.maximumGain(s="cdbcbbaaabab", x=4, y=5) == 19

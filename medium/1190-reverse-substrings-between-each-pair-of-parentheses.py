'''
反转每对括号间的子串
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

 

示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
 

提示：

0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的
'''
from collections import deque
'''
思路：递归+队列
从左往右遍历字符串，普通字符按照当前的括号深度决定是顺序连结还是逆序连结，遇到括号递归处理
连结字符串使用双向队列辅助，如果是顺利连结，从右侧进入队列，如果是逆序连结，从左侧进入队列

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)

        def process(start, depth):
            queue = deque()
            while start < n:
                while start < n and s[start] != '(' and s[start] != ')':
                    if depth & 1:  # 奇数层逆序连结
                        queue.appendleft(s[start])
                    else:  # 偶数层顺序连结
                        queue.append(s[start])
                    start += 1
                if start == n:
                    break
                if s[start] == '(':  # 遇到左括号，递归处理
                    pair = process(start + 1, depth + 1)
                    if depth & 1:  # 奇数层逆序连结
                        queue.appendleft(pair[0])
                    else:  # 偶数层顺序连结
                        queue.append(pair[0])
                    start = pair[1]
                elif s[start] == ')':  # 遇到右括号，返回上一层
                    break
            return (''.join(queue), start + 1)  # 返回当前函数已处理的子字符串+当前函数已处理到的索引

        return process(0, 0)[0]


s = Solution()
print(s.reverseParentheses("ta()usw((((a))))"))
print(s.reverseParentheses("(abcd)"))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("(ed(et(oc))el)"))
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q") == 'apmnolkjihgfedcbq')

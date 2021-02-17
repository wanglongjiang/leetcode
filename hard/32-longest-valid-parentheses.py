'''
最长有效括号

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

'''
'''
思路：因只有小括号，可以将左括号'('视为height+1，右括号')'视为height-1,height>=1的情况下才能执行')'的减一。
每成功匹配一次')'，生成上下界limit = [index-1, index]尝试加入堆栈stack：
stack出栈，上一次匹配的上下界preLimit=[preLeft, preRight]
如果preRight==limitLeft,说明本次匹配的括号包含上一次匹配，将上下界修改为[preLeft-1,limitRight],然后入栈。
    这种情况下的入栈，因为上界向前扩展了，所以还需要依次向前搜索堆栈，直到没有发生边界扩展
如果preRight+1==limitLeft，说明本次匹配与上次匹配相邻，可以合并，将上下界修改为[preLeft, limitRight]，入栈
最后一种情况下，两次匹配不相邻，分别将preLimit和limit入栈

字符串遍历完成后，扫描堆栈，将相邻的上下界合并，并挑选出最大的长度
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        limits = []

        def push(limit):
            if limits:
                preLimit = limits.pop()
                if preLimit[1] == limit[0]:
                    limit = [preLimit[0] - 1, limit[1]]
                    push(limit)
                elif preLimit[1] + 1 == limit[0]:
                    limits.append([preLimit[0], limit[1]])
                else:
                    limits.append(preLimit)
                    limits.append(limit)
            else:
                limits.append(limit)

        height = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                height += 1
            else:
                if height > 0:
                    height -= 1
                    limit = [i - 1, i]
                    push(limit)
        maxLen = 0
        for limit in limits:
            maxLen = max(maxLen, limit[1] - limit[0] + 1)
        return maxLen


s = Solution()
print(s.longestValidParentheses("(((((())(()))))"))
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))
print(s.longestValidParentheses("(((((())(())(((((((()))"))

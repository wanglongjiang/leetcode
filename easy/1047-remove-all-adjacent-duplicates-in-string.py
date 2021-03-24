'''
删除字符串中的所有相邻重复项
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
'''
'''
思路1，暴力删除法。遇到相同的连续字母，从字符串中删除，然后从删除的上一个字符重新开始搜索。
    时间复杂度：每个字符最多遍历2次，最多会创建n/2个临时字符串，创建临时字符串的时间如果为O(1)则时间复杂度为O(n)，
        如果创建临时字符串的时间复杂度为O(n)，需要O(n^3)时间
    空间复杂度：O(n)，每次创建的临时字符串，下次会丢弃，创建新的。
思路2，栈。创建1个栈，保存字符下标。
    遇到的每个字符，与栈顶下标指向的字符对比，
        如果相同，出栈，抛弃该下标和当前下标。
        如果不同，入栈
    最后栈中剩余的下标，即为要保留的字符。
    时间复杂度：O(n)，每个下标最多入栈、出栈1次。
    空间复杂度：O(n)
思路3，对思路2再进行优化，不入下标，直接保存，时间复杂度与上面相同
'''


class Solution:
    # 思路3，栈
    def removeDuplicates(self, S: str) -> str:
        if S:
            stack = [S[0]]
            for i in range(1, len(S)):
                if stack and stack[-1] == S[i]:
                    stack.pop()
                else:
                    stack.append(S[i])
            S = ''.join(stack)
        return S

    # 思路2，栈
    def removeDuplicates2(self, S: str) -> str:
        if S:
            stack = [0]
            for i in range(1, len(S)):
                if stack and S[stack[-1]] == S[i]:
                    stack.pop()
                else:
                    stack.append(i)
            S = ''.join([S[i] for i in stack])
        return S

    # 思路1，暴力删除
    def removeDuplicates1(self, S: str) -> str:
        i = 0
        while i + 1 < len(S):
            if S[i] != S[i + 1]:
                i += 1
            else:
                S = S[:i] + S[i + 2:]
                if i > 0:
                    i -= 1
        return S


s = Solution()
print(s.removeDuplicates("abbaca"))
print(s.removeDuplicates("abba"))

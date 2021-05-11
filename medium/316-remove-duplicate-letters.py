'''
去除重复字母

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 10^4
s 由小写英文字母组成
'''
'''
思路：栈
目的：尽量让前面的字符按照升序出现。
首先需要遍历依次字符串，对所有字符进行计数
然后再次遍历字符串，对于每个字符，如果与栈顶相比是升序，入栈。
与栈顶相同，抛弃，计数减一
与栈顶相比是降序，且栈顶可以出栈（栈顶字符计数大于1），栈顶字符出栈
如果栈顶字符不能出栈，抛弃当前字符，计数减一
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        stack = []
        instack = set()
        n, i = len(s), 0
        while i < n:
            if not stack or stack[-1] < s[i]:  # 升序
                if s[i] not in instack:  # 在栈中不存在才入栈
                    stack.append(s[i])
                    instack.add(s[i])
                else:  # 在栈中已存在，抛弃
                    counter[s[i]] -= 1
                i += 1
            elif stack[-1] == s[i]:  # 相同，抛弃
                counter[s[i]] -= 1
                i += 1
            else:  # 降序
                if counter[stack[-1]] > 1:  # 栈顶元素剩余数量多于1个，出栈
                    instack.remove(stack[-1])
                    counter[stack.pop()] -= 1
                else:  # 栈顶元素只剩一个，不能出栈
                    if counter[s[i]] > 1:  # 当前元素多于1个，可以抛弃
                        counter[s[i]] -= 1
                    else:  # 当前元素只剩一个，不能抛弃，入栈
                        stack.append(s[i])
                        instack.add(s[i])
                    i += 1
        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("bcabc"))

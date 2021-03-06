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
from collections import Counter
'''
思路：单调栈 哈希
目的：尽量让前面的字符按照升序出现。
首先需要遍历依次字符串，对所有字符进行计数
然后再次遍历字符串，对于每个字符，
如果没有出现在栈内，且与栈顶相比是升序，入栈
如果没有出现在栈内，且与栈顶元素相比是降序，需要尝试将栈顶元素出栈（出栈的条件是该元素在后面还有）

与下面的题目相同：
- 1081.[不同字符的最小子序列](medium/1081-smallest-subsequence-of-distinct-characters.py)

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        instack = set()
        counter = Counter(s)
        ans = []
        for c in s:
            if c not in instack:
                while ans and ans[-1] > c and counter[ans[-1]] > 1:
                    counter[ans[-1]] -= 1
                    instack.remove(ans.pop())
                ans.append(c)
                instack.add(c)
            else:
                counter[c] -= 1
        return ''.join(ans)


s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("bcabc"))

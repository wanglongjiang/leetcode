'''
不同字符的最小子序列
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 1000
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

与下面的题相同：
- 316.[去除重复字母](medium/316-remove-duplicate-letters.py)

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
print(s.smallestSubsequence("bcbcbcababa") == "bca")
print(s.smallestSubsequence("ecbacba") == "eacb")
print(s.smallestSubsequence("cbacdcbc"))
print(s.smallestSubsequence("bcabc"))

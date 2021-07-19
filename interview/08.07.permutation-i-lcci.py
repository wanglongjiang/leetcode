'''
面试题 08.07. 无重复字符串的排列组合

无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
'''
from typing import List
'''
思路：回溯
每次回溯从剩余字符串中提取一个字符，附加到字符串后面

时间复杂度：O(n!)
空间复杂度：O(n)除了返回结果外，需要n空间作为回溯的辅助空间
'''


class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []

        def backtrack(s, remainder):
            m = len(remainder)
            if m == 1:
                s.append(remainder)
                ans.append(''.join(s))
                s.pop()
                return
            for i in range(m):
                s.append(remainder[i])
                backtrack(s, remainder[:i] + remainder[i + 1:])
                s.pop()

        backtrack([], S)
        return ans


s = Solution()
print(s.permutation('qwe'))
print(s.permutation('ab'))

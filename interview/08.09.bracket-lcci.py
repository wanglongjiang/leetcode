'''
面试题 08.09. 括号
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
from typing import List
'''
思路：回溯
设left、right2个变量，代表当前剩余的左括号、右括号的数量，它们初始都是n
进行回溯时，分别执行减少left和减少right2个分支（减少前，确保left>0,right>0,right>left)

时间复杂度：O(2^n)
空间复杂度：O(n)
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(left, right, s):
            if left == 0 and right == 0:
                ans.append(s)
                return
            if left > 0:
                backtrack(left - 1, right, s + "(")
            if right > 0 and right > left:
                backtrack(left, right - 1, s + ')')

        backtrack(n, n, '')
        return ans


s = Solution()
print(s.generateParenthesis(3))

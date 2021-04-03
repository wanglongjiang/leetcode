'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8
'''
from typing import List
'''
思路：回溯
排序后回溯，去重
时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def permutation(self, s: str) -> List[str]:
        li = list(s)
        li.sort()
        n = len(s)
        ans = set()

        def backtrack(i):
            for j in range(i, n):
                if i != j and li[i] != li[j]:
                    li[i], li[j] = li[j], li[i]
                    ans.add(''.join(li))
                backtrack(i + 1)
                if i != j and li[i] != li[j]:
                    li[i], li[j] = li[j], li[i]

        ans.add(''.join(li))
        backtrack(0)
        return list(ans)


s = Solution()
print(s.permutation('aac'))
print(s.permutation('abc'))
print(s.permutation('aaa'))

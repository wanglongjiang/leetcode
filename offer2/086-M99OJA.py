'''
剑指 Offer II 086. 分割回文子字符串
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "google"
输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
示例 2：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 3：

输入：s = "a"
输出：[["a"] 
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
 

注意：本题与主站 131 题相同： https://leetcode-cn.com/problems/palindrome-partitioning/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/M99OJA
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：回溯+记忆表
1、判断字符串中下标i开始的任意长度的字串是否为回文串，并保存到记忆表里面
2、回溯所有的子串组合，判断是否为回文串
时间复杂度：O(n^3)，第1个过程复杂度为O(n*(n^2+(n-1)^2+(n-2)^2+...+1)/2)=n*(n+1)*(2*n+1)/12，第2个过程也是O(n^3)
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        seq = []
        # 迭代所有可能子串，并判断是否回文，保存起来
        mem = [0] * n
        for i in range(n):
            mem[i] = [True] * (n - i)
            for j in range(i + 2, n + 1):
                subLen = (j - i) // 2
                for k in range(subLen):
                    if s[i + k] != s[j - k - 1]:
                        mem[i][j - i - 1] = False
                        break

        # 回溯
        def backtrack(k: int):
            for i in range(k + 1, n + 1):
                if mem[k][i - k - 1]:
                    if i == n:
                        seq.append(s[k:i])
                        ans.append(seq.copy())
                        seq.pop()
                    else:
                        seq.append(s[k:i])
                        backtrack(i)
                        seq.pop()

        backtrack(0)
        return ans

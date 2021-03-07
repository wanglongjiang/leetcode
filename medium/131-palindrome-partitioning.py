'''
分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。
'''
from typing import List
'''
思路：回溯+记忆表
1、判断字符串中下标i开始的任意长度的字串是否为回文串，并保存到记忆表里面
2、回溯所有的子串组合，判断是否为回文串
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


s = Solution()
print(s.partition("aab"))
print(s.partition("aabb"))

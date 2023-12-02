from typing import List
'''
思路：模拟
模拟题意，遍历所有单词

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxLen = max(map(len, words))
        mat = [[' ' for _ in range(maxLen)] for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words[i])):
                mat[i][i] = words[i][j]
        return [''.join(mat[i]).rstrip() for i in range(len(mat))]

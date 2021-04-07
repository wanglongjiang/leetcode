'''
重复的DNA序列
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，
识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
'''
from typing import List
'''
思路1，暴力搜索
针对每个位置开始的10个字符，都搜索s整个字符串。
时间复杂度：O(n^2)，因为s最大大小达到10^5，会超出时间限制
TODO
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pass

'''
最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
'''
from typing import List
'''
思路1，信息压缩+暴力计算
因单词中只有小写字母，可以将每个字母压缩为整数上的1bit，压缩后对比2个单词是否有重复字母只需要2个整数与就可以
然后用2重循环，对比每一对单词是否有相同字符，如果没有重复的字符再计算乘积

复杂度：
> 时间复杂度：O(n*k+n*n)，n为words.length，k为单词平均长度
> 空间复杂度：O(n)
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        lengths, compressed = [0] * n, [0] * n
        # 信息压缩
        base = ord('a')
        for i in range(n):
            lengths[i] = len(words[i])
            for c in words[i]:
                compressed[i] |= 1 << (ord(c) - base)
        # 暴力对比
        ans = 0
        for i in range(1, n):
            for j in range(i):
                if compressed[i] & compressed[j] == 0:
                    ans = max(ans, lengths[i] * lengths[j])
        return ans

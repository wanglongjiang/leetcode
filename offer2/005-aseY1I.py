'''
剑指 Offer II 005. 单词长度的最大乘积
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

 

示例 1:

输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
示例 2:

输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: words = ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
 

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母
 

注意：本题与主站 318 题相同：https://leetcode-cn.com/problems/maximum-product-of-word-lengths/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/aseY1I
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路1，状态压缩
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

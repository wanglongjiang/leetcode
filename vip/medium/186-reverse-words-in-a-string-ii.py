'''
186. 翻转字符串里的单词 II
给定一个字符串，逐个翻转字符串中的每个单词。

示例：

输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
注意：

单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的
进阶：使用 O(1) 额外空间复杂度的原地解法。
'''
from typing import List
'''
思路：脑筋急转弯 两次翻转
需要2次翻转，有点像高老爷子在书里说的翻手掌算法
第1次，将整个数组翻转，经过1次翻转后，单词的位置符合了题意，但单词内的字符反了；
第2次，遍历每个单词，将单词内部的字符进行翻转，经过这样操作后，每个单词又恢复了正常。

时间复杂度：O(n),需要遍历2次数组
空间复杂度：O(1)
'''


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()  # 第1次翻转
        left, right, n = 0, 0, len(s)
        while right < n:
            while right < n and s[right] != ' ':  # 找到单词右边界
                right += 1
            k = right - 1
            while left < k:  # 翻转单词内的字符
                s[left], s[k] = s[k], s[left]
                left += 1
                k -= 1
            right += 1
            left = right


s = Solution()
arr = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
s.reverseWords(arr)
print(arr)

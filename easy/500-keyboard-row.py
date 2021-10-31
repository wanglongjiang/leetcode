'''
500. 键盘行
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
American keyboard



示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]


提示：

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成
'''
from typing import List
'''
思路：字符串
设每个单词的第1个字符在第row行，整个单词所有的字符所在行数与row如果相同则输出到结果中

时间复杂度：O(mn)
空间复杂度：O(1)
'''


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for word in words:
            w = word.lower()
            row = 0 if w[0] in keyboards[0] else (1 if w[0] in keyboards[1] else 2)
            for char in w:
                if row != (0 if char in keyboards[0] else (1 if char in keyboards[1] else 2)):
                    break
            else:
                ans.append(word)
        return ans


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

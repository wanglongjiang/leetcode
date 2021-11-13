'''
520. 检测大写字母
我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如 "USA" 。
单词中所有字母都不是大写，比如 "leetcode" 。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。



示例 1：

输入：word = "USA"
输出：true
示例 2：

输入：word = "FlaG"
输出：false


提示：

1 <= word.length <= 100
word 由小写和大写英文字母组成
'''
import re
'''
思路：正则表达式
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (re.match(r'^[A-Z](([A-Z]*)|([a-z]*))$', word) or re.match(r'^[a-z]+$', word)) is not None


s = Solution()
print(s.detectCapitalUse('USA'))
print(s.detectCapitalUse('FlaG'))

'''
面试题 17.13. 恢复空格
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

 

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
提示：

0 <= len(sentence) <= 1000
dictionary中总字符数不超过 150000。
你可以认为dictionary和sentence中只包含小写字母。
'''
from typing import List
'''
思路：字典树
1. 将dictionary中所有单词加入字典树
2. 遍历sentence每一个位置，如果找到匹配（有可能1个位置能匹配多个单词），需要从这多个匹配后的位置依次出发再次匹配。每个匹配完成后，都需要更新最少未匹配字符数。

TODO

时间复杂度：O(m+n^2)
空间复杂度：O(m)
'''


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie, endIds = {}, set()

        # 单词加入字典树
        def add(word):
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            endIds.add(id(node))

        # 查找所有的匹配
        def lookup(word) -> List:
            pass

        ans = float('inf')

        # 回溯匹配在字典树中所有的匹配
        def backtrack(index):
            pass

        return ans

'''
面试题 16.02. 单词频率

设计一个方法，找出任意指定单词在一本书中的出现频率。

你的实现应该支持如下操作：

WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
get(word)查询指定单词在书中出现的频率
提示：

book[i]中只包含小写字母
1 <= book.length <= 100000
1 <= book[i].length <= 10
get函数的调用次数不会超过100000
'''
from typing import List
'''
思路：哈希表或者字典树
用字典树应该更快一点，这里偷个懒，用计数器
'''


class WordsFrequency:
    def __init__(self, book: List[str]):
        from collections import Counter
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter.get(word, 0)

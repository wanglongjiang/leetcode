'''
字符流
按下述要求实现 StreamChecker 类：

StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，包括刚刚查询的字母）拼写出给定字词表中的某一字词时，返回 true。否则，返回 false。
 

示例：

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // 初始化字典
streamChecker.query('a');          // 返回 false
streamChecker.query('b');          // 返回 false
streamChecker.query('c');          // 返回 false
streamChecker.query('d');          // 返回 true，因为 'cd' 在字词表中
streamChecker.query('e');          // 返回 false
streamChecker.query('f');          // 返回 true，因为 'f' 在字词表中
streamChecker.query('g');          // 返回 false
streamChecker.query('h');          // 返回 false
streamChecker.query('i');          // 返回 false
streamChecker.query('j');          // 返回 false
streamChecker.query('k');          // 返回 false
streamChecker.query('l');          // 返回 true，因为 'kl' 在字词表中。
 

提示：

1 <= words.length <= 2000
1 <= words[i].length <= 2000
字词只包含小写英文字母。
待查项只包含小写英文字母。
待查项最多 40000 个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stream-of-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：字典树
words中的逆序词加入trie
query中的字符依次加入list,然后逆序查找trie中是否有单词存在。

初始化时间复杂度：O(words.length*words[i].length)
query时间复杂度：O(n)
'''


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.ends = set()
        self.q = []
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.trie
        for c in word[::-1]:
            if c not in node:
                node[c] = {}
            node = node[c]
        self.ends.add(id(node))

    def lookup(self):
        node = self.trie
        for i in range(len(self.q) - 1, -1, -1):
            c = self.q[i]
            if c not in node:
                return False
            node = node[c]
            if id(node) in self.ends:
                return True
        return False

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        return self.lookup()

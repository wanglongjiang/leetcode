'''
实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
'''
'''
思路1，用数组实现，空间浪费比较多，速度比较快，更换字符集需要改写程序
思路2，使用哈希表实现，空间浪费稍，速度比上面的数组方式慢，更换字符集不需要改写程序
'''


class Trie:
    def __init__(self):
        self.root = {}
        self.finishs = set()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {}  # 每个新增节点都是dict
            node = node[word[i]]
        if id(node) not in self.finishs:  # 因为python不支持将dict作为key，这里取它的id作为key插入终点集合
            self.finishs.add(id(node))

    def search(self, word: str) -> bool:
        if not word:
            return True
        node = self.root
        for i in range(len(word)):
            if word[i] not in node:
                return False
            node = node[word[i]]
        return id(node) in self.finishs

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node:
                return False
            node = node[prefix[i]]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))

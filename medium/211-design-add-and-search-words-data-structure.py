'''
添加与搜索单词 - 数据结构设计
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；
否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
'''
'''
思路：字典树trie的变形
使用字典树的变形，查找时对'.'进行特殊处理，
'''


class WordDictionary:
    def __init__(self):
        self.root = {}
        self.finishs = set()

    def addWord(self, word: str) -> None:
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
        n = len(word)

        def backtrack(i, node):
            if word[i] == '.':
                if i == n - 1:  # 最后一个字符是通配符，需要检查node内的所有字符是否为终点
                    for nextNode in node.values():
                        if id(nextNode) in self.finishs:
                            return True
                    return False
                for nextNode in node.values():
                    if backtrack(i + 1, nextNode):
                        return True
                return False
            elif word[i] not in node:  # 普通字符不匹配，返回false
                return False
            elif i == n - 1:  # 是最后一个字符，查看是否为终点
                return id(node[word[i]]) in self.finishs
            else:  # 不是终点，需要进一步匹配
                return backtrack(i + 1, node[word[i]])

        return backtrack(0, self.root)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
print(wordDictionary.search("bad"))
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))

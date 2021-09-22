'''
剑指 Offer II 062. 实现前缀树
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
inputs = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
 

 

注意：本题与主站 208 题相同：https://leetcode-cn.com/problems/implement-trie-prefix-tree/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/QC3q1f
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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

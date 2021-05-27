'''
键值映射

实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
 

示例：

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

提示：

1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum
'''
'''
思路：字典树
创建字典树，insert操作会将key,value插入字典树
sum操作会遍历所有以prefix开头的词在字典树中的值，然后求值之和

时间复杂度：insert函数为O(n),n为单个词长度；sum函数为O(nk)，n为prefix长度，k为平均每个prefix的单词个数
'''


class MapSum:
    def __init__(self):
        self.trie = {}
        self.kv = {}

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        self.kv[id(node)] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for c in prefix:
            if c not in node:
                node = None
                break
            node = node[c]
        if node is not None:
            return self.sumAll(node)
        return 0

    # 递归遍历求node的所有子节点值之和
    def sumAll(self, node):
        ans = 0
        if id(node) in self.kv:
            ans += self.kv[id(node)]
        for v in node.values():
            ans += self.sumAll(v)
        return ans


s = MapSum()
s.insert('apple', 3)
print(s.sum('apple'))
s.insert('app', 2)
print(s.sum('ap'))

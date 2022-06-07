'''
2227. 加密解密字符串
给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。
另给你一个字符串数组 dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。

字符串 加密 按下述步骤进行：

对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。
在字符串中，用 values[i] 替换字符 c 。
字符串 解密 按下述步骤进行：

将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。
如果存在多个有效的 i ，从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
在字符串中，用 keys[i] 替换 s 。
实现 Encrypter 类：

Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和 dictionary 初始化 Encrypter 类。
String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。
 

示例：

输入：
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
输出：
[null, "eizfeiam", 2]

解释：
Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // 返回 "eizfeiam"。 
                           // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
encrypter.decrypt("eizfeiam"); // return 2. 
                              // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为 'd'。 
                              // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和 "cbcd"。 
                              // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以答案是 2 。
 

提示：

1 <= keys.length == values.length <= 26
values[i].length == 2
1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
所有 keys[i] 和 dictionary[i] 互不相同
1 <= word1.length <= 2000
1 <= word2.length <= 200
所有 word1[i] 都出现在 keys 中
word2.length 是偶数
keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母
至多调用 encrypt 和 decrypt 总计 200 次
'''
from collections import defaultdict
from typing import List
'''
思路：字典树
加密过程很简单。
解密如果采用暴力把所有word2的组合都找出来，时间或空间复杂度能达到O(26^100)。
所以这里采用字典树，将dictionary所有单词加入字典树。每次解密最多遍历整个字典树，时间复杂度为O(dictionary.length)

复杂度分析：
encrypt 时间复杂度：O(word1.length)
decrypt 时间复杂度：O(word2.length+dictionary.length)
'''


class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.kv, self.vk = {}, defaultdict(list)  # 设置2个哈希表，将key和value，value对应的多个key保存
        for i in range(len(keys)):
            self.kv[keys[i]] = values[i]
            self.vk[values[i]].append(keys[i])
        self.trie = {}  # 字典树，用于保存dictionary
        self.endNodes = set()  # 字典树的终结节点
        for word in dictionary:  # 遍历所有单词，将其加入字典树
            node = self.trie
            for ch in word:
                if ch in node:
                    node = node[ch]
                else:
                    node[ch] = {}
                    node = node[ch]
            self.endNodes.add(id(node))

    def encrypt(self, word1: str) -> str:
        ans = []
        for ch in word1:
            ans.append(self.kv[ch])
        return ''.join(ans)

    def decrypt(self, word2: str) -> int:
        return self.lookup(word2, self.trie)

    def lookup(self, word, trieNode):
        ans = 0
        for ch in self.vk[word[0:2]]:
            if ch in trieNode:
                if len(word) == 2:  # 当前字符是最后一个
                    if id(trieNode[ch]) in self.endNodes:  # 如果当前字符为最后一个字符，整个单词为合法的
                        ans += 1
                else:  # 当前字符不是最后一个，需要递归向下查找后面的字符
                    ans += self.lookup(word[2:], trieNode[ch])
        return ans


encrypter = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
print(encrypter.encrypt("abcd"))
print(encrypter.decrypt("eizfeiam"))

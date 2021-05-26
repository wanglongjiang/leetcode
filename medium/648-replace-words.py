'''
单词替换

在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，
可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

 

示例 1：

输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 2：

输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
示例 3：

输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
输出："a a a a a a a a bbb baba a"
示例 4：

输入：dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 5：

输入：dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
输出："it is ab that this solution is ac"
 

提示：

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写字母组成。
1 <= sentence.length <= 10^6
sentence 仅由小写字母和空格组成。
sentence 中单词的总量在范围 [1, 1000] 内。
sentence 中每个单词的长度在范围 [1, 1000] 内。
sentence 中单词之间由一个空格隔开。
sentence 没有前导或尾随空格。
'''
from typing import List
'''
思路：字典树
1. 将dictionary中的单词加入字典树
2. 遍历sentence，查询其中的单词是否出现在字典树中，如果字典树中有单词，将其替换原单词。

时间复杂度：O(26mn+l),m为dictionary.length，n为dictionary[i]平均长度，l为sentence.length
空间复杂度：O(mn+l)
'''


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieCount, trieSize, charsetSize = 0, len(dictionary) * 100, 26
        trie = [[0] * charsetSize for _ in range(trieSize)]
        finishIds = set()

        # 添加单词到字典树
        def add(word):
            nonlocal trieCount
            nodeId = 0
            for i in range(len(word)):
                c = ord(word[i]) - ord('a')
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                else:
                    trieCount += 1
                    trie[nodeId][c] = trieCount
                    nodeId = trieCount
            finishIds.add(nodeId)

        end = len(sentence)

        # 从index开始查询sentence是否存在于字典树
        def search(index):
            nodeId = 0
            while index < end:
                c = ord(sentence[index]) - ord('a')
                if trie[nodeId][c]:
                    nodeId = trie[nodeId][c]
                    if nodeId in finishIds:
                        return index + 1
                    index += 1
                else:
                    return -1
            return -1

        # 1. 添加单词到字典树
        for word in dictionary:
            add(word)
        # 2. 遍历sentence，替换掉字典树中存在的单词
        start = 0
        ans = []
        while start < end:
            rootEnd = search(start)
            if rootEnd >= 0:  # 找到词根
                ans.append(sentence[start:rootEnd])  # 词根输出到结果list
                start = rootEnd
                while start < end and sentence[start] != ' ':  # 跳过词根后面的字符
                    start += 1
            else:  # 未找到词根
                wordEnd = start + 1
                while wordEnd < end and sentence[wordEnd] != ' ':  # 找到单词末尾
                    wordEnd += 1
                ans.append(sentence[start:wordEnd])
                start = wordEnd
            if start < end:
                start += 1  # 跳过空格
        return ' '.join(ans)


s = Solution()
print(s.replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs") == "a a b c")
print(s.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery") == "the cat was rat by the bat")
print(s.replaceWords(dictionary=["a", "aa", "aaa", "aaaa"], sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa") == "a a a a a a a a bbb baba a")
print(s.replaceWords(dictionary=["catt", "cat", "bat", "rat"], sentence="the cattle was rattled by the battery") == "the cat was rat by the bat")
print(s.replaceWords(dictionary=["ac", "ab"], sentence="it is abnormal that this solution is accepted") == "it is ab that this solution is ac")

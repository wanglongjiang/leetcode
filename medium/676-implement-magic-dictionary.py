'''
实现一个魔法字典
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，
请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：

MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，
使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
 

示例：

输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
 

提示：

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写英文字母组成
dictionary 中的所有字符串 互不相同
1 <= searchWord.length <= 100
searchWord 仅由小写英文字母组成
buildDict 仅在 search 之前调用一次
最多调用 100 次 search
'''
from typing import List
'''
思路：哈希
buildDict:将dictionary中每个word的每个字符依次替换成一个占位符'-'，然后将其加入哈希表
search:将当前单词的每个字符依次替换成占位符'-'，然后查找上面的哈希表中是否存在

时间复杂度：O(mnn),m为dictionary,n为dictionary.length
时间复杂度：O(mnn)
'''


class MagicDictionary:
    def __init__(self):
        self.dicts = [set() for _ in range(100)]
        self.orig = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.orig.add(word)
            for i in range(len(word)):
                self.dicts[i].add(word[:i] + '-' + word[i + 1:])

    def search(self, searchWord: str) -> bool:
        if searchWord in self.orig:
            return False
        for i in range(len(searchWord)):
            wd = searchWord[:i] + '-' + searchWord[i + 1:]
            if wd in self.dicts[i]:
                return True
        return False

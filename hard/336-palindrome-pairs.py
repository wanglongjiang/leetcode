'''
回文对
给定一组 互不相同 的单词， 找出所有 不同 的索引对 (i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

 

示例 1：

输入：words = ["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：words = ["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
示例 3：

输入：words = ["a",""]
输出：[[0,1],[1,0]]
 
提示：

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] 由小写英文字母组成

'''
from typing import List
from collections import defaultdict
'''
思路：字典树
1. 将所有的word逆序加入字典树，每加入一个字符，就将当前前缀对应的word索引记录下来。
2. 用word查询字典树，当能检索到最后，检查以word为前缀的所有逆序字符串剩余的子串是否为回文串

时间复杂度：O(nm)
空间复杂度：O(nm)
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        trie, endIds = {}, set()
        prefixNodeIndexs = defaultdict(list)

        # 添加字符串到字典树中
        def add(word, index):
            node = trie
            prefixNodeIndexs[id(node)].append(index)
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in node:
                    node[word[i]] = {}
                node = node[word[i]]
                prefixNodeIndexs[id(node)].append(index)
            endIds.add(id(node))

        for i in range(n):
            add(words[i], i)

        def isPalindrome(word, postfixLen):
            i, j = 0, len(word) - postfixLen - 1
            while i <= j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True

        ans = []
        # 查询word，当能检索到最后，检查以word为前缀的所有逆序字符串剩余的子串是否为回文串
        for i in range(n):
            word = words[i]
            m = len(word)
            if m == 0:
                for j in range(n):
                    if len(words[j]) > 0 and isPalindrome(words[j], 0):  # 空字符串与任何回文串都能构成回文串
                        ans.append([j, i])
                        ans.append([i, j])
                break
            node = trie
            for j in range(m):
                if word[j] not in node:
                    break
                node = node[word[j]]
            else:
                # 检查以word为前缀的所有字符串，剩余部分是否为回文串
                for j in prefixNodeIndexs[id(node)]:
                    if i != j and isPalindrome(words[j], m):
                        ans.append([i, j])
        return ans


s = Solution()
print(s.palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))  # 长度为6？
print(s.palindromePairs(["a", ""]))
print(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(s.palindromePairs(["abcd", "dcba", "s", "lls", "sssll"]))
print(s.palindromePairs(["bat", "tab", "cat"]))

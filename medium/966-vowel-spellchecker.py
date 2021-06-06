'''
元音拼写检查器
在给定单词列表 wordlist 的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。

对于给定的查询单词 query，拼写检查器将会处理两类拼写错误：

大小写：如果查询匹配单词列表中的某个单词（不区分大小写），则返回的正确单词与单词列表中的大小写相同。
例如：wordlist = ["yellow"], query = "YellOw": correct = "yellow"
例如：wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
例如：wordlist = ["yellow"], query = "yellow": correct = "yellow"
元音错误：如果在将查询单词中的元音（‘a’、‘e’、‘i’、‘o’、‘u’）分别替换为任何元音后，
能与单词列表中的单词匹配（不区分大小写），则返回的正确单词与单词列表中的匹配项大小写相同。
例如：wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
例如：wordlist = ["YellOw"], query = "yeellow": correct = "" （无匹配项）
例如：wordlist = ["YellOw"], query = "yllw": correct = "" （无匹配项）
此外，拼写检查器还按照以下优先级规则操作：

当查询完全匹配单词列表中的某个单词（区分大小写）时，应返回相同的单词。
当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。
当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。
如果该查询在单词列表中没有匹配项，则应返回空字符串。
给出一些查询 queries，返回一个单词列表 answer，其中 answer[i] 是由查询 query = queries[i] 得到的正确单词。

 

示例：

输入：wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
输出：["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
 

提示：

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
wordlist 和 queries 中的所有字符串仅由英文字母组成。
'''
from typing import List
'''
思路：哈希
建立3个哈希表：
第1个：将wordlist中的word保持原貌加入
第2个：将word全部转为小写加入，重复的全部在一个list中
第3个：将元音全部转为减号'-'加入，重复的key全部在一个list中

查询时，首先查询hash1如果存在，将原值返回
如果hash1中不存在，转为小写查询hash2，如果存在，返回list第1个
如果hash2中不存在，将元音转为减号'-'在hash3中查询，如果存在，返回list第1个
如果3个hash都不存在，返回空字符串

时间复杂度：O(m+n)，m为wordlist.length,n为queries.length
空间复杂度：O(m)
'''


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # word加入3个哈希表
        hash1, hash2, hash3 = set(), {}, {}
        for word in wordlist:
            hash1.add(word)
            lowWord = word.lower()
            if lowWord not in hash2:
                hash2[lowWord] = word
            novWord = ''
            for c in lowWord:
                if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                    novWord += '-'
                else:
                    novWord += c
            if novWord not in hash3:
                hash3[novWord] = word
        # 查询
        ans = [''] * len(queries)
        for i in range(len(queries)):
            if queries[i] in hash1:
                ans[i] = queries[i]
            else:
                lowWord = queries[i].lower()
                if lowWord in hash2:
                    ans[i] = hash2[lowWord]
                else:
                    novWord = ''
                    for c in lowWord:
                        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                            novWord += '-'
                        else:
                            novWord += c
                    if novWord in hash3:
                        ans[i] = hash3[novWord]
        return ans

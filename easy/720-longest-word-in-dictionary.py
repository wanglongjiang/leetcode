'''
词典中最长的单词
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

 

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释:
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
 

提示：

所有输入的字符串都只包含小写字母。
words数组长度范围为[1,1000]。
words[i]的长度范围为[1,30]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序 哈希
1. 将words中的单词按照长度排序。
2. 遍历排序后的words，对于当前单词word
> 如果word去掉末尾字符形成的单词在哈希表hashset中存在
>> 将其与以保存的ans进行对比，如果word的长度更长或者字典序更小，将ans替换为word，同时将word加入hashset
> 如果word去掉末尾字符形成的单词在哈希表hashset中不存在，该word不符合条件，需要抛弃

时间复杂度：O(mn),m为words.length,n为words[i]的长度
空间复杂度：O(mn)，需要用哈希表保存单词
'''


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: len(word))
        hashset, ans = set(), ''
        for word in words:
            if len(word) == 1:
                hashset.add(word)
                if len(word) > len(ans) or ans > word:
                    ans = word
            else:
                if word[:len(word) - 1] in hashset:
                    hashset.add(word)
                    if len(word) > len(ans) or ans > word:
                        ans = word
        return ans


s = Solution()
print(
    s.longestWord([
        "ts", "e", "x", "pbhj", "opto", "xhigy", "erikz", "pbh", "opt", "erikzb", "eri", "erik", "xlye", "xhig", "optoj", "optoje", "xly", "pb", "xhi", "x", "o"
    ]))

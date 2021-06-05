'''
通过删除字母匹配到字典里最长单词
给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。

 

示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
示例 2：

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
 

提示：

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s 和 dictionary[i] 仅由小写英文字母组成
'''
from typing import List
'''
思路：字符串+排序
1. 对dictionary中字符串按照长度从长到短排序
2. 遍历dictionary中字符串，当前字符串为word，依次与s进行对比，
> 如果能匹配上，将当前字符串与之前的字符串进行对比，
>> 如果长度超过之前的字符串，则替换
>> 如果长度相同，字典序更小，则替换
如果遍历过程中，发现当前字符串word长度已经不大于成功的字符串，则中断对比

时间复杂度：O(mn)，m为dictionary.length，n为dictionary[i].length平均长度
空间复杂度：O(1)
'''


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda word: len(word), reverse=True)  # 对单词按照长度递减排序
        k = len(s)
        ans = ''
        for word in dictionary:
            i, j = 0, 0
            n = len(word)
            while i < n and j < k:  # 匹配word和s，如果遇到不同的字符，尝试跳过s的一些字符
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == n:  # 匹配成功
                if n > len(ans) or (n == len(ans) and ans > word):
                    ans = word
        return ans


s = Solution()
print(s.findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]))
print(s.findLongestWord(s="abpcplea", dictionary=["a", "b", "c"]))

'''
单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：哈希表
设哈希表wordMap，key为s中的单词，val为pattern中的字符
用空格分割s，遍历所有的单词：
> 如果单词在wordMap中不存在，假如wordMap
> 如果单词在wordMap中存在，且val与pattern对应的字符相同，跳过；如果不相同，返回false

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        wordMap, usedPattern = {}, set()
        for i, word in enumerate(words):
            if word in wordMap:
                if wordMap[word] != pattern[i]:
                    return False
            else:
                if pattern[i] in usedPattern:
                    return False
                wordMap[word] = pattern[i]
                usedPattern.add(pattern[i])
        return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))

'''
916. 单词子集
我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。

现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior” 的子集，但不是 “world” 的子集。

如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。

你可以按任意顺序以列表形式返回 A 中所有的通用单词。



示例 1：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
输出：["facebook","google","leetcode"]
示例 2：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
输出：["apple","google","leetcode"]
示例 3：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
输出：["facebook","google"]
示例 4：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
输出：["google","leetcode"]
示例 5：

输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
输出：["facebook","leetcode"]


提示：

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] 和 B[i] 只由小写字母组成。
A[i] 中所有的单词都是独一无二的，也就是说不存在 i != j 使得 A[i] == A[j]。
'''
from typing import List
from collections import Counter
'''
思路：哈希
用一个哈希表b统计words2中的所有字符的并集，单个字符个数保留最大值。
然后遍历words1，每个单词保护b中所有字符，且字符个数>=b中的字符个数则为通用单词

时间复杂度：O(mn+ln)，l=words1.length,m=words2.lenght,n=words1[i].length
空间复杂度：O(1)
'''


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b = {}
        for counter in map(Counter, words2):
            for char, count in counter.items():
                if char not in b or b[char] < count:
                    b[char] = count
        ans = []
        for word in words1:
            counter = Counter(word)
            for char, count in b.items():
                if char not in counter or counter[char] < count:
                    break
            else:
                ans.append(word)
        return ans


s = Solution()
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]))
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]))
print(s.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"]))

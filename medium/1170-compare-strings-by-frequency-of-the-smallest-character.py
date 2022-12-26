'''
1170. 比较字符串最小字母出现频次
定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。

例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，
需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。

请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。

 

示例 1：

输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
示例 2：

输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
 

提示：

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j]、words[i][j] 都由小写英文字母组成
'''
from bisect import bisect_right
from typing import List
'''
思路：哈希 排序 二分查找
1、定义函数f，计算words中每个word的结果，保存到数组中并排序
2、遍历queries，对于每个query，计算其f(query)，然后二分查找words的结果，得到其前面的结果的个数

时间复杂度：O(mlogn+nlogn)，m为queries的长度，n为words的长度
空间复杂度：O(n)
'''


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            char, count = word[0], 0
            for ch in word:
                if ch == char:
                    count += 1
                elif ch < char:
                    char = ch
                    count = 1
            return count

        points = list(sorted(f(word) for word in words))
        return list(len(points) - bisect_right(points, f(q)) for q in queries)


s = Solution()
print(s.numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))

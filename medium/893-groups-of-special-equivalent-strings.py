'''
893. 特殊等价字符串组
给你一个字符串数组 words。

一步操作中，你可以交换字符串 words[i] 的任意两个偶数下标对应的字符或任意两个奇数下标对应的字符。

对两个字符串 words[i] 和 words[j] 而言，如果经过任意次数的操作，words[i] == words[j] ，那么这两个字符串是 特殊等价 的。

例如，words[i] = "zzxy" 和 words[j] = "xyzz" 是一对 特殊等价 字符串，因为可以按 "zzxy" -> "xzzy" -> "xyzz"
的操作路径使 words[i] == words[j] 。
现在规定，words 的 一组特殊等价字符串 就是 words 的一个同时满足下述条件的非空子集：

该组中的每一对字符串都是 特殊等价 的
该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，
那么这个字符串就 不会 与该组内任何字符串特殊等价）
返回 words 中 特殊等价字符串组 的数量。



示例 1：

输入：words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
输出：3
解释：
其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。
另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。
示例 2：

输入：words = ["abc","acb","bac","bca","cab","cba"]
输出：3
解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]


提示：

1 <= words.length <= 1000
1 <= words[i].length <= 20
所有 words[i] 都只由小写字母组成。
所有 words[i] 都具有相同的长度。
'''
from typing import List
from collections import defaultdict
'''
思路：哈希 并查集
从题目中得知，字符串的奇数下标可以任意交换，偶数下标可以任意交换。
那么，2个字符串，只要奇数下标的字符数量、种类相同，偶数下标的字符数量、种类相同，这2个字符串就是特殊等价的。
可以用哈希表分别对奇数下标和偶数下标的字符进行计数，转成字符串，保存到哈希表中。
将特殊等价的字符串用并查集关联起来，最后统计并查集中的数量即可。

时间复杂度：O(mn)，m=words.length,n=words[i].length
空间复杂度：O(mn)
'''


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        uf = UnionFind(len(words))
        hashmap = defaultdict(int)
        for i, word in enumerate(words):
            odd, even = defaultdict(int), defaultdict(int)
            for j, char in enumerate(word):  # 分别对奇数偶数下标字符进行计数
                if j % 2:
                    odd[char] += 1
                else:
                    even[char] += 1
            # 下面这行代码把计数转为一个字符串，如odd,even分别是：{'a':1,'b':2}，{'c':1,'d':2}，转化为'a1b2-c1d2'
            key = ''.join(map(lambda p: p[0] + str(p[1]), sorted(odd.items()))) + '-' ''.join(map(lambda p: p[0] + str(p[1]), sorted(even.items())))
            if key not in hashmap:
                hashmap[key] = i
            else:
                uf.union(hashmap[key], i)  # 找到特殊等价字符串，加入并查集
        subsets = set()
        for i in range(len(words)):
            subsets.add(uf.find(i))  # 统计特殊等价字符串的索引
        return len(subsets)


# 定义并查集
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


s = Solution()
print(s.numSpecialEquivGroups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))
print(s.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))

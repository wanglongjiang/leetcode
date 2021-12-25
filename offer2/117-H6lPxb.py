'''
剑指 Offer II 117. 相似的字符串
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给定一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个 字母异位词 。请问 strs 中有多少个相似字符串组？

字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。

 

示例 1：

输入：strs = ["tars","rats","arts","star"]
输出：2
示例 2：

输入：strs = ["omv","ovm"]
输出：1
 

提示：

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] 只包含小写字母。
strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
   

注意：本题与主站 839 题相同：https://leetcode-cn.com/problems/similar-string-groups/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/H6lPxb
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：并查集
1、首先2重循环暴力检查是否相似，将相似结果加入并查集
2、检查并查集中有多少个集合


时间复杂度：O(n*n*m)，n=strs.length,m=strs[i].length，主要的时间都耗费在检查是否相似
空间复杂度：O(n)
'''


# 定义并查集
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)

        # 判断是否相似
        def isLike(s1, s2):
            m = len(s1)
            cnt = 0
            for i in range(m):
                if s1[i] != s2[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 2 or cnt == 0

        # 判断任意2个字符串是否相似，相似的字符串进入并查集
        for i in range(n):
            for j in range(i + 1, n):
                if isLike(strs[i], strs[j]):
                    uf.unite(i, j)
        # 检查并查集中有多少个集合
        allset = set()
        for i in range(n):
            allset.add(uf.find(i))
        return len(allset)


s = Solution()
print(s.numSimilarGroups(["abc", "abc"]))
print(s.numSimilarGroups(["tars", "rats", "arts", "star"]))
print(s.numSimilarGroups(["omv", "ovm"]))

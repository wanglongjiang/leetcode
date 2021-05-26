'''
面试题 17.07. 婴儿名字

每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，
例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。
给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。
注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择 字典序最小 的名字作为真实名字。

 

示例：

输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
 

提示：

names.length <= 100000
'''
from typing import List
from collections import defaultdict
'''
思路：并查集
非常典型的可以用并查集解决的问题。
1. 遍历names将其拆分成名字realNames和出现频率counts；并将名字和索引加入哈希表
2. 创建与名字相同大小的并查集，并查集中索引为realNames的索引
3. 遍历synonyms，将其加入并查集，确保字典序较小的作为父节点
4. 遍历realNames，如果通过并查集查找其根节点就是自身，加入结果哈希表，如果根节点不是自身，将其真实名称个数+1
5. 最后，输出结果哈希表

时间复杂度：O(n)
空间复杂度：O(n)
'''


# 定义并查集
class UnionFind:
    def __init__(self, n, realNames):
        self.n = n
        self.parent = list(range(n))
        self.realNames = realNames

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if self.realNames[rooti] > self.realNames[rootj]:  # 确保字典序较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        n = len(names)
        realNames, counts = [], []
        idxMap = {}
        # 1. 拆分名字、频率
        for i in range(n):
            realNames.append(names[i][:names[i].find('(')])
            counts.append(int(names[i][len(realNames[-1]) + 1:len(names[i]) - 1]))
            idxMap[realNames[-1]] = i
        # 2. 创建并查集
        unionFind = UnionFind(n, realNames)
        # 3. 遍历synonyms，将其加入并查集
        for synonym in synonyms:
            pair = synonym.split(',')
            name1, name2 = pair[0][1:], pair[1][:-1]
            if name1 in idxMap and name2 in idxMap:  # 别名列表中有可能有未出现在names中，需要跳过
                unionFind.unite(idxMap[name1], idxMap[name2])
        # 4. 累计真实名称个数
        counter = defaultdict(int)
        for i in range(n):
            counter[unionFind.find(i)] += counts[i]
        # 5. 输出真实名称个数
        ans = []
        for k, v in counter.items():
            ans.append(realNames[k] + '(' + str(v) + ')')
        return ans


s = Solution()
print(
    s.trulyMostPopular(names=["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
                       synonyms=["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]))

'''
按公因数计算最大组件大小
给定一个由不同正整数的组成的非空数组 A，考虑下面的图：

有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
返回图中最大连通组件的大小。

 

示例 1：

输入：[4,6,15,35]
输出：4

示例 2：

输入：[20,50,9,63]
输出：2

示例 3：

输入：[2,3,6,7,4,12,21,39]
输出：8

 

提示：

1 <= A.length <= 20000
1 <= A[i] <= 100000
'''
from typing import List
from collections import Counter
'''
并查集
1. 遍历所有的整数，将其所有的因子找出（从2开始一直到sqrt(num)），然后将整数的所有因子加入并查集。经过处理后，拥有相同的因子的整数会拥有同一个root中。
2. 遍历所有整数，查询并查集，对其root进行计数，最后输出最大的1个。

时间复杂度：O(nsqrt(n))
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
    def largestComponentSize(self, A: List[int]) -> int:
        unionFind = UnionFind(max(A) + 1)
        # 将num和它的所有因子加入并查集
        for num in A:
            minFactor = float('inf')
            if num > 2 and num % 2 == 0:
                minFactor = 2
                unionFind.unite(2, num)
                unionFind.unite(2, num >> 1)
            for i in range(3, int(num**0.5) + 1):
                d, r = divmod(num, i)
                if r == 0:
                    if minFactor > i:
                        minFactor = i
                        unionFind.unite(minFactor, num)
                    else:
                        unionFind.unite(minFactor, i)
                    unionFind.unite(minFactor, d)
        counter = Counter()
        for num in A:
            counter[unionFind.find(num)] += 1
        return counter.most_common(1)[0][1]


s = Solution()
print(s.largestComponentSize([32, 5, 8, 11, 13, 78, 61, 16, 83, 22, 28, 93]) == 9)
print(s.largestComponentSize([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6)
print(s.largestComponentSize([4, 6, 15, 35]) == 4)
print(s.largestComponentSize([20, 50, 9, 63]) == 2)
print(s.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]) == 8)

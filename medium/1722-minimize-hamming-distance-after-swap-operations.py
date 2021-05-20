'''
执行交换操作后的最小汉明距离
给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，
其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。
注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素.

相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。
形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。

在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。

 

示例 1：

输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
输出：1
解释：source 可以按下述方式转换：
- 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
- 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。

示例 2：
输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
输出：2
解释：不能对 source 执行交换操作。
source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。

示例 3：
输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
输出：0
 

提示：

n == source.length == target.length
1 <= n <= 10^5
1 <= source[i], target[i] <= 10^5
0 <= allowedSwaps.length <= 10^5
allowedSwaps[i].length == 2
0 <= ai, bi <= n - 1
ai != bi

'''
from typing import List
from collections import defaultdict
'''
思路：并查集
allowedSwaps里面的下标连结了若干元素，这些元素在这些下标处可以任意交换位置，也就是说，针对这些下标，每个下标都有一个集合可以选。
可以将allowedSwaps里面的下标用并查集连结起来，然后用最小的下标作为key，同一集合里面的下标作为value加入哈希表。
这样针对target的每个元素，查找其下标所指向的集合中是否有该元素，如果不存在汉明距离+1

时间复杂度：O(n)
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
            if rooti > rootj:
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        # 建立可交换节点的并查集
        union = UnionFind(n)
        for pair in allowedSwaps:
            union.unite(pair[0], pair[1])
        # 将每个下标能匹配的集合统计出来
        allowedSet = defaultdict(dict)
        for i in range(n):
            if source[i] in allowedSet[union.find(i)]:
                allowedSet[union.find(i)][source[i]] += 1
            else:
                allowedSet[union.find(i)][source[i]] = 1
        # 查找target每个元素是否能够匹配
        ans = 0
        for i in range(n):
            if target[i] not in allowedSet[union.find(i)]:
                ans += 1
            else:  # 将已匹配的删除
                allowedSet[union.find(i)][target[i]] -= 1
                if allowedSet[union.find(i)][target[i]] == 0:
                    del allowedSet[union.find(i)][target[i]]
        return ans


s = Solution()
print(s.minimumHammingDistance([2, 3, 1], [1, 2, 2], [[0, 2], [1, 2]]))
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]))
print(s.minimumHammingDistance(source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]))
print(s.minimumHammingDistance(source=[5, 1, 2, 4, 3], target=[1, 5, 4, 2, 3], allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]))

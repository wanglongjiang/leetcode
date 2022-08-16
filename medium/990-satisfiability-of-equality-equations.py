'''
990. 等式方程的可满足性
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。



示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true


提示：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='
'''
from typing import List
'''
思路：并查集
2个变量相等，可以认为2个变量连通了。
2个变量不相等，认为2个变量之间没有连通。
解决连通性问题的套路就是用并查集。

首先将equations中的等式加入并查集，然后验证不等式是否成立。

时间复杂度：O(n)
空间复杂度：O(1)，因为小写字母只有26个，也就是变量只有26个，并查集的大小固定为26
'''


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        neqs = []
        uf = UnionFind()
        for e in equations:
            if e[1] == '!':  # 不等式加入list待处理
                neqs.append(e)
            else:  # 等式加入并查集
                uf.union(e[0], e[3])
        for e in neqs:  # 遍历所有不等式，检查是否成立
            if uf.isUnion(e[0], e[3]):
                return False
        return True


# 定义并查集
class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def isUnion(self, a, b):
        i, j = ord(a) - ord('a'), ord(b) - ord('a')
        return self.find(i) == self.find(j)

    def union(self, a, b):
        i, j = ord(a) - ord('a'), ord(b) - ord('a')
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


s = Solution()
print(s.equationsPossible(["a==b", "b!=a"]))
print(s.equationsPossible(["b==a", "a==b"]))
print(s.equationsPossible(["a==b", "b==c", "a==c"]))
print(s.equationsPossible(["a==b", "b!=c", "c==a"]))
print(s.equationsPossible(["c==c", "b==d", "x!=z"]))

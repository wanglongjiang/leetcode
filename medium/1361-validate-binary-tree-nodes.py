'''
1361. 验证二叉树
二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。



示例 1：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true
示例 2：



输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false
示例 3：



输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false
示例 4：



输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false


提示：

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
'''
from typing import List
'''
思路：
根据题目中的输入，知道每个节点最多有2个子节点。
但有可能会出现环路，有可能会出现1个节点有多个父节点，这2种情况都是非法的。

算法描述：
1. 设一个并查集，用于保存节点的父子关系
2. 遍历每个节点：
> 如果出现leftChild或rightChild为其自身，有自环，是非法的
> 查询并查集中当前节点的根节点，如果出现当前节点的子节点是根节点，出现了环路，是非法的
> 如果子节点已经在并查集中，且其根节点并非自身，则子节点有多个父节点，是非法的
3. 最后再遍历所有节点，如果出现多个根则返回false

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for i in range(n):
            if leftChild[i] == i or rightChild[i] == i:  # 自环
                return False
            root = uf.find(i)
            if leftChild[i] == root or rightChild[i] == root:  # 环路
                return False
            if leftChild[i] >= 0:
                if uf.find(leftChild[i]) != leftChild[i]:  # 子节点有多个父节点
                    return False
                uf.union(i, leftChild[i])
            if rightChild[i] >= 0:
                if uf.find(rightChild[i]) != rightChild[i]:  # 子节点有多个父节点
                    return False
                uf.union(i, rightChild[i])
        root = uf.find(0)
        for i in range(1, n):  # 验证是否有多个根节点
            if root != uf.find(i):
                return False
        return True


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
            self.parent[rootj] = rooti


s = Solution()
print(s.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(s.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(s.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(s.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))

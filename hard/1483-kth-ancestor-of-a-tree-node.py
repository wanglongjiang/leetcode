'''
树节点的第 K 个祖先
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

 

示例：



输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
 

提示：

1 <= k <= n <= 5*10^4
parent[0] == -1 表示编号为 0 的节点是根节点。
对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
0 <= node < n
至多查询 5*10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：稀疏表+DFS
设稀疏表st，st[i][j]的意思是节点i的第2^j个祖先。
在初始化函数里面，需要深度优先遍历树，构建稀疏表st。
时间复杂度：O(nlogn)

getKthAncestor，从node出发，递归向上遍历求第k个父节点。
时间复杂度：O(logk)
'''


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # 将树的结构存储到邻接表中
        tree = [[] for _ in range(len(parent))]
        root = 0
        for node, p in enumerate(parent):
            if p == -1:
                root = node
            else:
                tree[p].append(node)

        # 构建稀疏表，需要dfs遍历树
        logn = self.getHighBit(n) + 1
        self.st = [[-1] * logn for _ in range(n)]

        def dfs(node, path):
            i = 0
            while (1 << i) <= len(path):
                idx = -(1 << i)
                self.st[node][i] = path[idx]  # 设置node的第2^i个父节点
                i += 1
            path.append(node)
            for child in tree[node]:
                dfs(child, path)
            path.pop()

        dfs(root, [])

    def getKthAncestor(self, node: int, k: int) -> int:
        logk = self.getHighBit(k)
        if k & (k - 1) == 0:  # k是2的幂，第k个祖先就保存在st[node][logk]中
            return self.st[node][logk]
        else:  # k不是2的幂，本层可以将最高位的1消掉
            p = self.st[node][logk]
            if p < 0:
                return -1
            else:
                return self.getKthAncestor(p, k ^ (1 << logk))  # 消掉最高位的1之后，递归向上搜索

    # 取出最高位的1的位置
    def getHighBit(self, n):
        i = 0
        if n & 0xffff0000:
            i += 16
            n &= 0xffff0000
        if n & 0xff00ff00:
            i += 8
            n &= 0xff00ff00
        if n & 0xf0f0f0f0:
            i += 4
            n &= 0xf0f0f0f0
        if n & 0xcccccccc:
            i += 2
            n &= 0xcccccccc
        if n & 0xaaaaaaaa:
            i += 1
        return i


s = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(s.getKthAncestor(3, 1))
print(s.getKthAncestor(5, 2))
print(s.getKthAncestor(6, 3))
print(s.getKthAncestor(1, 5))
print(s.getKthAncestor(6, 1))

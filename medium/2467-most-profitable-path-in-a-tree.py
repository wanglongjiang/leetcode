'''
2467. 树上最大得分和路径
中等
7
相关企业
一个 n 个节点的无向树，节点编号为 0 到 n - 1 ，树的根结点是 0 号节点。给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 在树中有一条边。

在每一个节点 i 处有一扇门。同时给你一个都是偶数的数组 amount ，其中 amount[i] 表示：

如果 amount[i] 的值是负数，那么它表示打开节点 i 处门扣除的分数。
如果 amount[i] 的值是正数，那么它表示打开节点 i 处门加上的分数。
游戏按照如下规则进行：

一开始，Alice 在节点 0 处，Bob 在节点 bob 处。
每一秒钟，Alice 和 Bob 分别 移动到相邻的节点。Alice 朝着某个 叶子结点 移动，Bob 朝着节点 0 移动。
对于他们之间路径上的 每一个 节点，Alice 和 Bob 要么打开门并扣分，要么打开门并加分。注意：
如果门 已经打开 （被另一个人打开），不会有额外加分也不会扣分。
如果 Alice 和 Bob 同时 到达一个节点，他们会共享这个节点的加分或者扣分。换言之，如果打开这扇门扣 c 分，那么 Alice 和 Bob 分别扣 c / 2 分。如果这扇门的加分为 c ，那么他们分别加 c / 2 分。
如果 Alice 到达了一个叶子结点，她会停止移动。类似的，如果 Bob 到达了节点 0 ，他也会停止移动。注意这些事件互相 独立 ，不会影响另一方移动。
请你返回 Alice 朝最优叶子结点移动的 最大 净得分。

 

示例 1：



输入：edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
输出：6
解释：
上图展示了输入给出的一棵树。游戏进行如下：
- Alice 一开始在节点 0 处，Bob 在节点 3 处。他们分别打开所在节点的门。
  Alice 得分为 -2 。
- Alice 和 Bob 都移动到节点 1 。
  因为他们同时到达这个节点，他们一起打开门并平分得分。
  Alice 的得分变为 -2 + (4 / 2) = 0 。
- Alice 移动到节点 3 。因为 Bob 已经打开了这扇门，Alice 得分不变。
  Bob 移动到节点 0 ，并停止移动。
- Alice 移动到节点 4 并打开这个节点的门，她得分变为 0 + 6 = 6 。
现在，Alice 和 Bob 都不能进行任何移动了，所以游戏结束。
Alice 无法得到更高分数。
示例 2：



输入：edges = [[0,1]], bob = 1, amount = [-7280,2350]
输出：-7280
解释：
Alice 按照路径 0->1 移动，同时 Bob 按照路径 1->0 移动。
所以 Alice 只打开节点 0 处的门，她的得分为 -7280 。
 

提示：

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges 表示一棵有效的树。
1 <= bob < n
amount.length == n
amount[i] 是范围 [-104, 104] 之间的一个 偶数 。
'''
from math import inf
from typing import List
'''
[TOC]

# 思路
DFS

# 解题方法
> 首先用DFS找到bob去往节点0的路径，记住这条路径上到每个节点的时间并保存到哈希表中
> 然后用DFS从0开始遍历alice的所有路径，如果中途遇到Bob遍历过的节点，需要根据规则计算得分


# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = [[] for _ in range(len(edges) + 1)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        # DFS找到bob去往节点0的路径，记住这条路径上到每个节点的时间并保存到哈希表中
        bobVisited = {}
        marked = set()

        def goto0(node, time):
            marked.add(node)
            if node == 0:
                return True
            for next in g[node]:
                if next not in marked:
                    if goto0(next, time + 1):
                        bobVisited[node] = time
                        return True

        goto0(bob, 0)
        ans = -inf
        marked = set()

        # DFS从0开始遍历alice的所有路径
        def dfs(node, time, score):
            nonlocal ans
            marked.add(node)
            if node in bobVisited:
                if bobVisited[node] == time:  # 同时到达节点，计算一半的分数
                    score += amount[node] // 2
                elif bobVisited[node] > time:  # alice先到达节点，全部得分
                    score += amount[node]
            else:  # 只有alice到达，计算得分
                score += amount[node]
            isLeaf = True
            for next in g[node]:
                if next not in marked:
                    isLeaf = False
                    dfs(next, time + 1, score)
            if isLeaf:
                ans = max(ans, score)

        dfs(0, 0, 0)
        return ans


s = Solution()
assert s.mostProfitablePath(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6]) == 6
assert s.mostProfitablePath(edges=[[0, 1]], bob=1, amount=[-7280, 2350]) == -7280

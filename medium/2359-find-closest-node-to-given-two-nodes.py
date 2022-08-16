'''
2359. 找到离给定两个节点最近的节点
给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。

有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。

同时给你两个节点 node1 和 node2 。

请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。

注意 edges 可能包含环。

 

示例 1：



输入：edges = [2,2,3,-1], node1 = 0, node2 = 1
输出：2
解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
示例 2：



输入：edges = [1,2,-1], node1 = 0, node2 = 2
输出：2
解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
 

提示：

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
'''
from typing import List
'''
思路：哈希
1、从node1出发，遍历所有能到达的节点，并记录与node1的距离
2、从node2出发，遍历所有能到达的节点，并记录与node2的距离
3、遍历上面2个节点出发能够到达的公共节点（交集），找到较大值最小的

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # 从node出发，遍历所有能到达的节点，并记录距离
        def each(node):
            distances, dis = {node: 0}, 1
            while edges[node] >= 0 and edges[node] not in distances:
                node = edges[node]
                distances[node] = dis
                dis += 1
            return distances

        dis1, dis2 = each(node1), each(node2)
        ans, minDis = -1, float('inf')
        for node, dis in dis1.items():
            if node in dis2:
                if max(dis2[node], dis) < minDis:  # 找到距离更近的
                    minDis = max(dis2[node], dis)
                    ans = node
                elif max(dis2[node], dis) == minDis and node < ans:  # 相同距离，取编号更小的
                    ans = node
        return ans


s = Solution()
print(s.closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2))
print(s.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))

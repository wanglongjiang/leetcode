'''
访问所有节点的最短路径
给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 

graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。

 

示例 1：

输入：[[1,2,3],[0],[0],[0]]
输出：4
解释：一个可能的路径为 [1,0,2,0,3]
示例 2：

输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一个可能的路径为 [0,1,4,2,3]
 

提示：

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：位运算 BFS 状态压缩
因为最多有12个节点，可以将遍历状态压缩为1个整数。
最终状态是(1<<n)-1，也就是低位有n个1。
从每个节点出发，暴力搜索所有的路径，直至所有节点被遍历完毕。

时间复杂度：O(2^n)，最坏情况下遍历n*2^n个状态
空间复杂度：O(2^n)，最坏情况下需要n*2^n个状态
'''


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q, nextq, ans = [(i, 1 << i) for i in range(n)], [], 0  # 将所有节点和初始状态加入队列待遍历
        finish = (1 << n) - 1  # 最终状态，达到这个状态后，所有的节点被遍历完
        hashset = set()  # 剪枝用，将已遍历过的状态加入哈希表，防止重复遍历
        while True:
            node, state = q.pop()
            if state == finish:
                return ans
            for nextnode in graph[node]:  # 遍历当前节点所有下一节点
                nextState = (nextnode, state | (1 << nextnode))  # 将下一节点的状态附加到当前状态上
                if nextState not in hashset:  # 剪枝，如果下一个节点的状态未遍历过，加入队列
                    hashset.add(nextState)
                    nextq.append(nextState)
            if not q:
                q, nextq = nextq, q
                ans += 1


s = Solution()
print(s.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
print(s.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))

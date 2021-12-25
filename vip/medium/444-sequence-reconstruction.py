'''
444. 序列重建
验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤ 10^4。
重建是指在序列集 seqs 中构建最短的公共超序列。（即使得所有  seqs 中的序列都是该最短序列的子序列）。
确定是否只可以从 seqs 重建唯一的序列，且该序列就是 org 。

示例 1：

输入：
org: [1,2,3], seqs: [[1,2],[1,3]]

输出：
false

解释：
[1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。


示例 2：

输入：
org: [1,2,3], seqs: [[1,2]]

输出：
false

解释：
可以重建的序列只有 [1,2]。


示例 3：

输入：
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

输出：
true

解释：
序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。


示例 4：

输入：
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

输出：
true
'''
from typing import List
from collections import deque
'''
思路：图 拓扑排序
1. seqs重建为有向图
2. 对seqs中的节点进行拓扑排序，排序过程中如果出现如下情况则不满足重建：
- seqs中的元素小于1或者大于n
- 同时出现2个入度为0的节点，也就是这2个节点的排序谁先谁后都可以，这种情况也是不可以的
- 出现环路
3. 最后对比seqs的拓扑排序结果是否与org相同

时间复杂度：O(n+e)，e为边的数量
空间复杂度：O(n+e)
'''


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs:
            return False
        n = len(org)
        g = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)  # 拓扑排序的辅助入度数组
        queue = deque()  # 拓扑排序的辅助队列
        for seq in seqs:
            this = seq[0]
            if this < 1 or this > n:
                return False
            for i in range(1, len(seq)):  # 遍历子序列，将前后路径加入图
                next = seq[i]
                if next < 1 or next > n:
                    return False
                g[this].append(next)
                indegree[next] += 1
                this = next
        for i in range(1, n + 1):
            if indegree[i] == 0:  # 入度为0的节点加入队列
                queue.append(i)
        ans = []
        while queue:
            if len(queue) > 1:  # 不能同时有2个入度为0的节点
                return False
            node = queue.popleft()
            ans.append(node)
            for next in g[node]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        if any(indegree):
            return False
        return ans == org

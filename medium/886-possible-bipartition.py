'''
可能的二分法
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

 

示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：

输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 

提示：

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
对于 dislikes[i] == dislikes[j] 不存在 i != j
'''
from typing import List
'''
思路：图的DFS遍历
在dislikes里面的节点对a,b，视为a,b之间有一条边。根据题意，直接相连的2个节点需要分配到2个组里面，如果不能分配到2个组里结果为False。
具体算法如下：
1. 建立大小为N的图g，然后将dislikes作为边加入到图g里。
2. 遍历g中每个节点，如果节点a被分配为1队，那么与其直接相连的节点集合都需要分配到2队，反之如果a被分配为2队，相连的节点分配为1队。
3. 在上面的遍历过程中，如果以往被分配过队伍的节点又被分配为其他队伍，说明无法分配为2队。

是785.[判断二分图](medium/785-is-graph-bipartite.py)的升级

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 1. 建立邻接表形式的图
        g = [[] for _ in range(n + 1)]
        for dis in dislikes:
            g[dis[0]].append(dis[1])
            g[dis[1]].append(dis[0])
        # 2. 遍历图中所有节点
        visited = [0] * (n + 1)

        def dfs(i, team):
            visited[i] = team
            nextteam = 1 if team == 2 else 2
            for nexti in g[i]:
                if visited[nexti]:  # 如果之前分配过队伍，且之前的队伍与本次想要分配的队伍不一致，分配失败
                    if visited[nexti] != nextteam:
                        return False
                else:
                    if not dfs(nexti, nextteam):
                        return False
            return True

        for i in range(1, n + 1):
            if not visited[i]:
                if not dfs(i, 1):
                    return False
        return True


s = Solution()
print(s.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
print(s.possibleBipartition(n=3, dislikes=[[1, 2], [1, 3], [2, 3]]))
print(s.possibleBipartition(n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))

'''
2285. 道路的最大总重要性
给你一个整数 n ，表示一个国家里的城市数目。城市编号为 0 到 n - 1 。

给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] 表示城市 ai 和 bi 之间有一条 双向 道路。

你需要给每个城市安排一个从 1 到 n 之间的整数值，且每个值只能被使用 一次 。道路的 重要性 定义为这条道路连接的两座城市数值 之和 。

请你返回在最优安排下，所有道路重要性 之和 最大 为多少。

 

示例 1：



输入：n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
输出：43
解释：上图展示了国家图和每个城市被安排的值 [2,4,5,3,1] 。
- 道路 (0,1) 重要性为 2 + 4 = 6 。
- 道路 (1,2) 重要性为 4 + 5 = 9 。
- 道路 (2,3) 重要性为 5 + 3 = 8 。
- 道路 (0,2) 重要性为 2 + 5 = 7 。
- 道路 (1,3) 重要性为 4 + 3 = 7 。
- 道路 (2,4) 重要性为 5 + 1 = 6 。
所有道路重要性之和为 6 + 9 + 8 + 7 + 7 + 6 = 43 。
可以证明，重要性之和不可能超过 43 。
示例 2：



输入：n = 5, roads = [[0,3],[2,4],[1,3]]
输出：20
解释：上图展示了国家图和每个城市被安排的值 [4,3,2,5,1] 。
- 道路 (0,3) 重要性为 4 + 5 = 9 。
- 道路 (2,4) 重要性为 2 + 1 = 3 。
- 道路 (1,3) 重要性为 3 + 5 = 8 。
所有道路重要性之和为 9 + 3 + 8 = 20 。
可以证明，重要性之和不可能超过 20 。
 

提示：

2 <= n <= 5 * 104
1 <= roads.length <= 5 * 104
roads[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
没有重复道路。
'''
from typing import List
'''
思路：贪心 排序
用贪心思路可以看出，一个城市的道路越多，它的数值越高越好。
所有道路重要性之和为sum(no[i]*edgeNum[i])，no[i]为第i个元素的编号，edgeNum[i]为它的道路数量。
edgeNum[i]是固定的，那么edgeNum[i]越大，no[i]越大更好。

具体算法是：
1、设一个数组edgeNum，edgeNum[i]为城市i的道路数。遍历一次roads数组，可以得到所有城市的道路数。
2、对edgeNum排序，道路数量从低到高，获得1..n的编号。再计算所有城市 编号*道路数量 的和。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edgeNum = [0] * n
        for road in roads:
            edgeNum[road[0]] += 1
            edgeNum[road[1]] += 1
        return sum(map(lambda p: (p[0] + 1) * p[1], enumerate(sorted(edgeNum))))

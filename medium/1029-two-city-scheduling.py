'''
两地调度

公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

 

示例：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
 

提示：

1 <= costs.length <= 100
costs.length 为偶数
1 <= costs[i][0], costs[i][1] <= 1000
'''
from typing import List
'''
思路：贪心
求A,B两个城市的费用差，diff，然后对diff排序，找出差最小的一半，也就是去往a最划算的一半人用a的价格结算，剩下一半用b的价格结算。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diffs = [(costs[i][0] - costs[i][1], i) for i in range(n)]
        diffs.sort(key=lambda item: item[0])
        ans = 0
        for i in range(n // 2):
            ans += costs[diffs[i][1]][0]
        for i in range(n // 2, n):
            ans += costs[diffs[i][1]][1]
        return ans


s = Solution()
print(s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))

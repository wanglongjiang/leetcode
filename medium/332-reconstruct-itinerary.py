'''
重新安排行程

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，
所以该行程必须从 JFK 开始。

 

提示：

如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次。
 

示例 1：

输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2：

输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
'''
from typing import List
'''
思路：图+排序
从1个机场出发的机票如果有若干张，需要按字典序排序，又，机票使用完一张后就不能再用。
可以将所有的机场构成一张有向图，每个节点是机场，每个机票是一个边，从机场出发的机票要按字典顺序进行排序，并加入队列中。
这样该题的算法是从JFK机场开始，按照从机票队列中拿出一张进入下一个机场，这样依次遍历所有机场。

时间复杂度：O(n+e)
空间复杂度：O(n+e)
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = {}
        # 机票加入图，并排序
        for ticket in tickets:
            if ticket[0] not in g:
                g[ticket[0]] = []
            if ticket[1] not in g:
                g[ticket[1]] = []
            g[ticket[0]].append(ticket[1])
        for li in g.values():
            li.sort()
        # 遍历机场
        ans = []

        def dfs(node):
            ans.append(node)
            if g[node]:
                nextnode = g[node][0]
                del g[node][0]
                dfs(nextnode)

        dfs('JFK')
        return ans


s = Solution()
print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

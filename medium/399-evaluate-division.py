'''
除法求值
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路：BFS
每个变量就是一个节点，如果A/B=2那么A与B之间有一条权重为2的边，B与A之间有一条权重为0.5的边。
求任意2个变量的除法的结果，可以搜索图中这2个节点之间路径的累积

时间复杂度：O(n*m)n为equations.length,m为queries.length
空间复杂度：O(m+n)
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []
        for i, e in enumerate(equations):
            graph[e[0]].append((e[1], values[i]))  # 将(变量，权重)加入节点的边列表中
            graph[e[1]].append((e[0], 1 / values[i]))  # 将(变量，权重)加入节点的边列表中
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                ans.append(-1)  # 两个变量都不在变量表中，输出-1
                continue
            marked = defaultdict(bool)
            marked[query[0]] = True
            q, nextq = [], []
            q.append((query[0], 1))
            while q:
                node, val = q.pop()
                if node == query[1]:
                    ans.append(val)
                    break
                for nextnode, nextval in graph[node]:
                    if not marked[nextnode]:
                        marked[nextnode] = True
                        q.append((nextnode, nextval * val))  # 将下一节点和边长的累积加入队列
                if not q:
                    q, nextq = nextq, q
            else:
                ans.append(-1)  # 未找到路径，输出-1
        return ans

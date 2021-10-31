'''
2049. 统计最高分的节点数目
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，
其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，
剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。



示例 1:

example-1

输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
示例 2：

example-2

输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。


提示：

n == parents.length
2 <= n <= 10^5
parents[0] == -1
对于 i != 0 ，有 0 <= parents[i] <= n - 1
parents 表示一棵二叉树。
'''
from typing import List
'''
思路：树的遍历
统计每个树的子树大小，每个树的积分= 当前节点所有子树大小乘积*（n-当前节点所有子树大小-1）
首先遍历parents数组，构造tree数组，tree数组中每个元素是一个list，保存节点的子节点
递归遍历tree，计算每个节点的子树大小，同时计算积分

时间复杂度：O(n)
空间复杂度：O(n)，需要tree保存树
'''


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parents[i]].append(i)
        points = [0] * n

        # 递归遍历所有节点，统计其子节点数和积分
        def helper(node):
            point = 1
            count = 1
            for nextnode in tree[node]:
                nodenum = helper(nextnode)
                count += nodenum
                point *= nodenum
            otherNodenum = n - count
            points[node] = point * (otherNodenum if otherNodenum else 1)
            return count

        helper(0)
        maxp = max(points)
        return sum(map(lambda p: 1 if p == maxp else 0, points))  # 统计最大积分的节点数量


s = Solution()
print(s.countHighestScoreNodes([-1, 2, 0, 2, 0]) == 3)
print(s.countHighestScoreNodes([-1, 2, 0]) == 2)

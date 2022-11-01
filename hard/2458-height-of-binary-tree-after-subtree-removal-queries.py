'''
2458. 移除子树后的二叉树高度
给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。

你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：

从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。
返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。

注意：

查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。
树的高度是从根到树中某个节点的 最长简单路径中的边数 。
 

示例 1：



输入：root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
输出：[2]
解释：上图展示了从树中移除以 4 为根节点的子树。
树的高度是 2（路径为 1 -> 3 -> 2）。
示例 2：



输入：root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
输出：[3,2,3,2]
解释：执行下述查询：
- 移除以 3 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 4）。
- 移除以 2 为根节点的子树。树的高度变为 2（路径为 5 -> 8 -> 1）。
- 移除以 4 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 6）。
- 移除以 8 为根节点的子树。树的高度变为 2（路径为 5 -> 9 -> 3）。
 

提示：

树中节点的数目是 n
2 <= n <= 105
1 <= Node.val <= n
树中的所有值 互不相同
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val
'''
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS 哈希表
首先用DFS遍历树，将每个子树的高度和层级记录到哈希表中，同时用一个数组记录每层子树最高的高度和数量，次高的树的高度。
然后遍历queries，对于每个查询，
- 首先查询该子树的高度，然后在数组中查询该层级子树的最高高度，如果该子树不是最高的，删掉子树对树的高度无影响
- 如果该子树是最高的之一，删掉子树对数的高度无影响
- 如果该子树是唯一最高的子树，需要取次高的树加上层级返回

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        treeHigh = {}  # 哈希表，key为节点值，value为2元组（子树高度，子树的层级）
        top2s = []  # 数组，元素为3元组（最高树的高度，最高树的数量，次高树的高度）

        def dfs(node, level):
            if not node:
                return 0
            if len(top2s) == level:  # 扩充top2s数组
                top2s.append((0, 0, 0))
            h = max(dfs(node.left, level + 1), dfs(node.right, level + 1)) + 1  # 计算当前树的高度，注意，这里计算出的高度是节点数，比题目中的多1
            treeHigh[node.val] = (h, level)
            if top2s[level][0] < h:  # 当前子树高于以往记录的最高高度，进行更新
                top2s[level] = (h, 1, top2s[level][0])
            elif top2s[level][0] == h:  # 当前子树等于以往记录的最高高度，更新数量
                top2s[level] = (h, top2s[level][1] + 1, top2s[level][2])
            elif top2s[level][2] < h:  # 当次高树的高度小于当前子树高度，更新次高树高度
                top2s[level] = (top2s[level][0], top2s[level][1], h)
            return h

        dfs(root, 0)
        ans = []
        for q in queries:
            h, level = treeHigh[q]
            firstHigh, firstCount, secondHigh = top2s[level]
            if h < firstHigh:
                ans.append(top2s[0][0] - 1)  # 该子树不是最高的，返回整树高度
            elif h == firstHigh and firstCount > 1:
                ans.append(top2s[0][0] - 1)  # 该子树并列最高，返回整树高度
            else:
                ans.append(level + secondHigh - 1)  # 该子树唯一最高，返回次高树高度+层级-1
        return ans


def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i] is not None:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.treeQueries(fromList([5, 8, 9, 2, 1, 3, 7, 4, 6]), [3, 2, 4, 8]))
print(s.treeQueries(fromList([1, 3, 4, 2, null, 6, 5, null, null, null, null, null, 7]), [4]))

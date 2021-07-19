'''
节点与其祖先之间的最大差值

给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

 

示例 1：



输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释：
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
示例 2：


输入：root = [1,null,2,null,0,3]
输出：3
 

提示：

树中的节点数在 2 到 5000 之间。
0 <= Node.val <= 105
'''
from sortedcontainers import SortedList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS+SortedList
DFS遍历所有节点，将从根节点到叶子节点的路径加入SortedList，记录遍历过程中的max(最大值-最小值)

时间复杂度：O(nlogh)h为树的高度
空间复杂度：O(h)h为树的高度
'''


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        path = SortedList()
        ans = 0

        def dfs(node):
            nonlocal ans
            path.add(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not node.left and not node.right:  # 到了叶子节点，计算最大差
                ans = max(path[-1] - path[0], ans)
            path.remove(node.val)

        dfs(root)
        return ans

'''
二叉树的堂兄弟节点
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
深度优先搜索分别找到2个节点，首先判断深度是否相同，再判断父节点相同

时间复杂度：O(n)
空间复杂度：平均情况下是O(logn)，最坏情况下是O(n)
'''


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xparent, yparent = None, None
        xDepth, yDepth = 0, 0

        def dfs(node, parent, depth):
            nonlocal xparent, yparent, xDepth, yDepth
            if node.val == x:
                xparent = parent
                xDepth = depth
            elif node.val == y:
                yparent = parent
                yDepth = depth
            if node.left:
                dfs(node.left, node, depth + 1)
            if node.right:
                dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        return xDepth == yDepth and xparent != yparent


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
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
null = None
print(s.isCousins(fromList([1, 2, 3, null, 4, null, 5]), 5, 4))

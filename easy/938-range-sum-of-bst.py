'''
二叉搜索树的范围和
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

提示：

树中节点数目在范围 [1, 2 * 104] 内
1 <= Node.val <= 105
1 <= low <= high <= 105
所有 Node.val 互不相同
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：遍历二叉搜索树
当前节点node与[low,high]关心有3种
val<low，当前节点与左子树都会小于low，则只需要再搜索右子树
val>high，当前节点与右子树都会大于high，只需要再搜索左子树
val介于low,high之间，需要将当前节点值+左子树+右子树

时间复杂度：O(n)
空间复杂度：O(logn)，最坏情况下树为线性结构，需要递归深度为O(n)
'''


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def sumTree(node):
            if node.val < low:
                return sumTree(node.right) if node.right else 0
            if node.val > high:
                return sumTree(node.left) if node.left else 0
            ans = node.val
            if node.left:
                ans += sumTree(node.left)
            if node.right:
                ans += sumTree(node.right)
            return ans

        return sumTree(root)

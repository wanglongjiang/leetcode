'''
左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \\
  9  20
    /  \\
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
递归遍历所有节点，如果当前节点的左节点是叶子节点合计返回其值，同时合计右子树的的左叶子节点

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node):
            val = 0
            if node.left:
                if not node.left.left and not node.left.right:
                    val += node.left.val
                else:
                    val += dfs(node.left)
            if node.right:
                val += dfs(node.right)
            return val

        return dfs(root)

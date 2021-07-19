'''
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \\
  9  20
    /  \\
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \\
     2   2
    / \\
   3   3
  / \\
 4   4
返回 false 。

 

限制：

0 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归遍历所有的分支，记录最低高度、最高高度。二者之差如果大于1则返回False
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        minHeight, maxHeight = float('inf'), float('-inf')

        def dfs(node, h):
            nonlocal minHeight
            nonlocal maxHeight
            if node.left:
                if not dfs(node.left, h + 1):
                    return False
            else:
                minHeight = min(h, minHeight)
                maxHeight = max(h, maxHeight)
                if maxHeight - minHeight > 1:
                    return False
            if node.right:
                if not dfs(node.right, h + 1):
                    return False
            else:
                minHeight = min(h, minHeight)
                maxHeight = max(h, maxHeight)
                if maxHeight - minHeight > 1:
                    return False
            return True

        if not root:
            return True
        return dfs(root, 1)

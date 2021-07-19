'''
面试题 04.04. 检查平衡性
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


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

与下面题目相同：
- 110.[平衡二叉树](easy/110-balanced-binary-tree.py)
- 剑指 Offer 55 - II.[平衡二叉树](offer/55-ping-heng-er-cha-shu-lcof.py)
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

'''
剑指 Offer 28. 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \\
  2   2
 / \\ / \\
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \\
  2   2
   \\   \\
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
可以分2步：
第1步：递归遍历左子树，将其左右交换
第2步：调用第100题的判断是否相同树的函数，对比2个子树
时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def exchange(node: TreeNode):
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    exchange(node.left)
                if node.right:
                    exchange(node.right)

        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            def helper(p, q):
                if not p and not q:
                    return True
                if not p or not q:
                    return False
                if p.val != q.val:
                    return False
                return helper(p.left, q.left) and helper(p.right, q.right)

            return helper(p, q)

        if not root:
            return True
        exchange(root.left)
        return isSameTree(root.left, root.right)

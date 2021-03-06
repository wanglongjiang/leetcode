'''
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：经过观察可以发现，左边子树的左右节点全部交换后，与右边子树相同
可以分2步：
第1步：遍历左子树，将其左右交换
第2步：调用第100题的判断是否相同树的函数，对比2个子树
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

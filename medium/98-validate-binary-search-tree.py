'''
验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：按照树的前序算法遍历验证
1、验证节点与左右节点的大小关系是否正确
2、验证节点与左右所有子节点大小关系是否正确（该验证会增加复杂度，待一次提交一次后确认是否需要添加）
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node: TreeNode):
            if node.left:
                if node.val <= node.left.val:
                    return False
                if not recursion(node.left):
                    return False
            if node.right:
                if node.val >= node.right.val:
                    return False
                if not recursion(node.right):
                    return False
            return True

        if not root:
            return False
        return recursion(root)


s = Solution()
print(s.isValidBST())

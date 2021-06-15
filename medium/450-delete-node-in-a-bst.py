'''
删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
按照二叉搜索树的性质，先查找节点，（大于当前节点搜索右子树，小于当前节点搜索左子树）
找到节点后，
> 如果左右子树都存在，将当前节点的左子树设置为当前树根节点，然后将右子树设置为原左子树的最大节点的右子树（因为右子树所有元素均大于左子树，这样能保持搜索树的性质）
> 如果只有1个子树，将该子树设置为根节点

时间复杂度：O(h)
空间复杂度：O(h)
'''


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        # 改变树的最大节点
        def changeMax(node, maxNode):
            if node.right:
                changeMax(node.right, maxNode)
            else:
                node.right = maxNode

        # 删除指定节点
        def delete(node):
            if node.val > key:  # 小于当前节点，搜索左子树
                if node.left:
                    node.left = delete(node.left)
            elif node.val < key:  # 大于当前节点，搜索右子树
                if node.right:
                    node.right = delete(node.right)
            else:  # 找到当前节点，当前树的根节点需要变更
                if not node.right or not node.left:
                    return node.right if node.right else node.left
                else:  # 左右子树都存在，将当前节点的左子树设置为当前树根节点，然后将右子树设置为左子树的最大节点的右子树
                    changeMax(node.left, node.right)
                    return node.left
            return node

        return delete(root)

'''
修剪二叉搜索树
给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，
使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构
（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
针对每个节点，
如果该节点的值<low，则该节点及左子树都需要删除，再递归处理右子树，如果右子树在区间内，需要返回右子树
如果该节点的值>high，则该节点及右子树都需要删除，再递归处理左子树，如果左子树在区间内，需要返回左子树
如果该节点值low<=val<=high，该节点需要保留，该节点的左节点为递归处理过的左子树，右节点为递归处理过的右子树
时间复杂度：O(n)
空间复杂度：O(h)，递归深度为树的高度
'''


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def recu(node: TreeNode):
            if not node:
                return None
            if node.val < low:  # 该节点<low，则该节点及左子树都要删除，返回右子树的处理结果
                return recu(node.right)
            if node.val > high:  # 该节点>high，则该节点及右子树都要删除，返回左子树的处理结果
                return recu(node.left)
            node.left = recu(node.left)
            node.right = recu(node.right)
            return node

        return recu(root)

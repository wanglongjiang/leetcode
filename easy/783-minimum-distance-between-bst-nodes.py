'''
二叉搜索树节点最小距离
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：深度优先遍历
二叉搜索树的左子树点小于本节点，右子树大于本节点
差值最小的肯定在节点与左子树的最大节点，节点与右子树的最小节点
深度优先遍历树,与之前的每个父节点对比
时间复杂度：O(nlogn)，或 O(n^2)，如果是平衡二叉树，需要O(nlogn)，最坏情况下是O(n^2)
空间复杂度：O(logn)，最坏情况下O(n)
'''


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        path = []
        minDiff = float('inf')

        def dfs(node: TreeNode):
            nonlocal minDiff
            for val in path:
                minDiff = min(minDiff, abs(val - node.val))
            if node.left or node.right:
                path.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                path.pop()

        dfs(root)
        return minDiff

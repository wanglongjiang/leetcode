'''
分裂二叉树的最大乘积

给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

 

示例 1：



输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
示例 2：



输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
示例 3：

输入：root = [2,3,9,10,7,8,6,5,4,11,1]
输出：1025
示例 4：

输入：root = [1,1]
输出：1
 

提示：

每棵树最多有 50000 个节点，且至少有 2 个节点。
每个节点的值在 [1, 10000] 之间。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS
1. 遍历整棵树，得到整个树的和total
2. 遍历树，求子树subtree，和整棵树剩余部分的乘积product = sum(subtree)*(total - sum(subtree))。在遍历的过程中记录最大乘积

时间复杂度：O(n)，2次遍历树
空间复杂度：O(h)，递归需要的栈空间为树的高度h
'''


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def sumTotal(node):
            return node.val + (sumTotal(node.left) if node.left else 0) + (sumTotal(node.right) if node.right else 0)

        total = sumTotal(root)
        ans = 0

        def product(node):
            nonlocal ans
            subtotal = node.val + (product(node.left) if node.left else 0) + (product(node.right) if node.right else 0)
            ans = max(ans, subtotal * (total - subtotal))
            return subtotal

        product(root)
        return ans

'''
祖父节点值为偶数的节点和

给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。

 

示例：



输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
 

提示：

树中节点的数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：DFS
深度优先遍历，将祖父节点的奇偶性传给节点，节点根据奇偶性进行计算

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, gp, p):
            nonlocal ans
            if gp:
                ans += node.val
            if node.left:
                dfs(node.left, p, node.val % 2 == 0)
            if node.right:
                dfs(node.right, p, node.val % 2 == 0)

        dfs(root, False, False)
        return ans

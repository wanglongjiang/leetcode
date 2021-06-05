'''
把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/  相同

 

示例 1：



输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
示例 2：

输入：root = [0,null,1]
输出：[1,null,1]
示例 3：

输入：root = [1,0,2]
输出：[3,3,2]
示例 4：

输入：root = [3,2,4,1]
输出：[7,9,4,10]
 

提示：

树中的节点数介于 1 和 100 之间。
每个节点的值介于 0 和 100 之间。
树中的所有值 互不相同 。
给定的树为二叉搜索树。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
从题目中可以了解到累加树的定义，一个节点的值是其原树中大于等于其node.val的值之和
也就是如果节点是上级的右子树，其和为node.val+右子树的累加+祖父节点累加
如果节点是上级的左子树，其和为node.val+右子树累计+父节点累计
根据上面的信息可以写出递归函数

时间复杂度：O(n)，所有节点都需要遍历一次
空间复杂度：O(logn)，递归深度为logn
'''


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recu(node: TreeNode, parentSum):
            if node.right:
                node.val += recu(node.right, parentSum)
            else:
                node.val += parentSum
            if node.left:
                return recu(node.left, node.val)
            return node.val

        if root:
            recu(root, 0)
        return root

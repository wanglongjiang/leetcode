'''
剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先
且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：树 递归
1. 先找到p节点，找到p节点的过程中记住从根节点到p的路径path
2. 从path的最后一个节点node开始，根据q与node的关系向左或向右搜索，如果找不到则从node上一个节点继续寻找

时间复杂度：O(h^2)
空间复杂度：O(h)
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. 查找p节点，并将根节点到p节点的路径记录到path中。p和q的最近公共祖先肯定在path中
        def lookupP(node, path):
            path.append(node)
            if node.val > p.val:
                lookupP(node.left, path)
            elif node.val < p.val:
                lookupP(node.right, path)

        path = []
        lookupP(root, path)

        # 2. 从path最后一个节点开始，按照二叉搜索树的性质，向左或向右搜索q节点
        def lookupQ(node):
            if node.val > q.val:
                if node.left:
                    return lookupQ(node.left)
                else:
                    return False
            elif node.val < q.val:
                if node.right:
                    return lookupQ(node.right)
                else:
                    return False
            return True

        while path:
            node = path.pop()
            if lookupQ(node):
                return node

'''
剑指 Offer II 047. 二叉树剪枝
给定一个二叉树 根节点 root ，树的每个节点的值要么是 0，要么是 1。请剪除该二叉树中所有节点的值为 0 的子树。

节点 node 的子树为 node 本身，以及所有 node 的后代。

 

示例 1:

输入: [1,null,0,0,1]
输出: [1,null,0,null,1]
解释:
只有红色节点满足条件“所有不包含 1 的子树”。
右图为返回的答案。


示例 2:

输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]
解释:


示例 3:

输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]
解释:


 

提示:

二叉树的节点个数的范围是 [1,200]
二叉树节点的值只会是 0 或 1
 

注意：本题与主站 814 题相同：https://leetcode-cn.com/problems/binary-tree-pruning/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pOCWxh
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
遍历树，将全部为0的子树删除

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            iszero = False
            if not node.val:
                iszero = True
            if node.left:
                if dfs(node.left):
                    node.left = None
                    iszero &= True
                else:
                    iszero = False
            if node.right:
                if dfs(node.right):
                    node.right = None
                    iszero &= True
                else:
                    iszero = False
            return iszero

        if dfs(root):
            return None
        return root

'''
另一棵树的子树
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

 

示例 1：


输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：


输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
 

提示：

root 树上的节点数量范围是 [1, 2000]
subRoot 树上的节点数量范围是 [1, 1000]
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
遍历父树的每个子树，查看是否与subRoot相同

时间复杂度：O(mn)，m为父树节点数，n为子树节点数
空间复杂度：O(h)
'''


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(node, subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val == subnode.val:
                if dfs(node.left, subnode.left) and dfs(node.right, subnode.right):
                    return True
            if node.left:
                if dfs(node.left, subnode):
                    return True
            if node.right:
                if dfs(node.right, subnode):
                    return True
            return False

        return dfs(root, subRoot)

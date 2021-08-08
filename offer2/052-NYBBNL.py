'''
剑指 Offer II 052. 展平二叉搜索树
给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

 

示例 1：



输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
示例 2：



输入：root = [5,1,7]
输出：[1,null,5,null,7]
 

提示：

树中节点数的取值范围是 [1, 100]
0 <= Node.val <= 1000
 

注意：本题与主站 897 题相同： https://leetcode-cn.com/problems/increasing-order-search-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/NYBBNL
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：后序遍历树
对于每个节点，先将右子树展开，返回值连结变成本节点的右节点
然后展开左子树，并将自身传入左子树展开过程，连结到右子树的尾部
时间复杂度：O(n)
空间复杂度：O(n)，最坏情况下堆栈深度为n
'''


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recu(node, greatParent):
            if node.right:
                node.right = recu(node.right, greatParent)
            else:
                node.right = greatParent
            if node.left:
                left = node.left
                node.left = None
                return recu(left, node)
            else:
                return node

        return recu(root, None)

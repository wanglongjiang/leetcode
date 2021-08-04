'''
单值二叉树
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
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
DFS递归遍历树，每个节点与其子节点的值是否相同

时间复杂度：O(n)
空间复杂度：O(h),h为树的高度，通常为logn
'''


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left:
            if root.val != root.left.val:
                return False
            if not self.isUnivalTree(root.left):
                return False
        if root.right:
            if root.val != root.right.val:
                return False
            if not self.isUnivalTree(root.right):
                return False
        return True

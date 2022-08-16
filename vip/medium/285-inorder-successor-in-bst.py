'''
二叉搜索树中的中序后继
给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。

节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。

 

示例 1：



输入：root = [2,1,3], p = 1
输出：2
解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
示例 2：



输入：root = [5,3,6,2,4,null,null,1], p = 6
输出：null
解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
 

提示：

树中节点的数目在范围 [1, 104] 内。
-10^5 <= Node.val <= 10^5
树中各节点的值均保证唯一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/P5rCT8
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
首先按照二叉搜索树的性质递归找到节点p，
然后有2种情况，
1. p有右子树，那么中序后续就是p的右子树的最小节点，需要递归查找。
2. p没有右子树，那么中序后续就是第1个大于p的父节点。

时间复杂度：O(logn)
空间复杂度：O(logn)
'''


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def findP(node):
            if node == p:
                if node.right:
                    return findMin(node.right)
                return None
            ans = None
            if node.val > p.val:
                ans = findP(node.left)
            else:
                ans = findP(node.right)
            if not ans and node.val > p.val:
                ans = node
            return ans

        def findMin(node):
            if node.left:
                return findMin(node.left)
            return node

        return findP(root)

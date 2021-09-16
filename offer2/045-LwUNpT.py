'''
剑指 Offer II 045. 二叉树最底层最左边的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

 

示例 1:



输入: root = [2,1,3]
输出: 1
示例 2:



输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 

提示:

二叉树的节点个数的范围是 [1,104]
-2^31 <= Node.val <= 231 - 1 
 

注意：本题与主站 513 题相同： https://leetcode-cn.com/problems/find-bottom-left-tree-value/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/LwUNpT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：树 DFS
树的DFS遍历，每一个节点如果当前节点深度高于以往遍历过的最深深度，更新值
时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        maxdepth, ans = 0, 0

        def dfs(node, depth):
            nonlocal maxdepth, ans
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
            if not node.left and not node.right:
                if depth > maxdepth:
                    maxdepth = depth
                    ans = node.val

        dfs(root, 1)
        return ans

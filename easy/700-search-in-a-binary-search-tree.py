'''
二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。
如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \\
      2   7
     / \\
    1   3

和值: 2
你应该返回如下子树:

      2
     / \\
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：迭代
按照搜索树的性质迭代向下查找

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    return None
            else:
                if root.right:
                    root = root.right
                else:
                    return None
        return None

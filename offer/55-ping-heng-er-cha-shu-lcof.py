'''
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \\
  9  20
    /  \\
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \\
     2   2
    / \\
   3   3
  / \\
 4   4
返回 false 。

 

限制：

0 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/

'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
思路：DFS递归遍历所有的分支，计算左右子树的高度。二者之差如果大于1则返回False
时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True

        def dfs(node, h):
            nonlocal ans
            leftH, rightH = h, h
            if node.left:
                leftH = dfs(node.left, h + 1)
            if node.right:
                rightH = dfs(node.right, h + 1)
            if abs(leftH - rightH) > 1:
                ans = False
            return max(leftH, rightH)

        if not root:
            return True
        dfs(root, 1)
        return ans


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i]:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


null = None
s = Solution()
print(s.isBalanced(fromList([3, 9, 20, None, None, 15, 7])))
print(s.isBalanced(fromList([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, null, null, 5, 5])))

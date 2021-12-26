'''
二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \\
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路1：递归
按照后序的定义，左右根的顺序遍历

时间复杂度：O(n)
空间复杂度：O(h)

思路2：迭代 栈
按照后序的定义，左右根的顺序遍历
用栈模拟函数的递归执行过程：
nodeStk保存当前节点
dirStk保存当前节点要遍历的方向：0为左树，1为右子树，2为自身

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    # 思路2，迭代
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans, nodeStk, dirStk = [], [], []
        if not root:
            return ans
        nodeStk.append(root)  # 根节点入栈
        dirStk.append(0)  # 根节点先从左子树开始遍历
        while nodeStk:
            if dirStk[-1] == 0:
                dirStk[-1] = 1  # 下一个方向为右子树
                if nodeStk[-1].left:
                    nodeStk.append(nodeStk[-1].left)
                    dirStk.append(0)  # 栈顶元素从左子树开始遍历
            elif dirStk[-1] == 1:
                dirStk[-1] = 2  # 下个方向为自身
                if nodeStk[-1].right:
                    nodeStk.append(nodeStk[-1].right)
                    dirStk.append(0)  # 栈顶元素从左子树开始遍历
            else:
                ans.append(nodeStk.pop().val)
                dirStk.pop()
        return ans

    # 思路1，递归
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans

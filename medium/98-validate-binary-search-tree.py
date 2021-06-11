'''
验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：递归
按照树的前序算法遍历验证
1、验证节点与左右节点的大小关系是否正确
2、验证节点与左右所有子节点大小关系是否正确，向递归过程传递当前子树最大值和最小值

时间复杂度：O(n)
空间复杂度：O(h)，h为树的高度
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not recursion(node.right, node.val, upper):
                return False
            if not recursion(node.left, lower, node.val):
                return False
            return True

        return recursion(root)


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


def toList(node: TreeNode):
    li = []
    if node is None:
        return li
    queue = [node]
    li.append(node.val)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        if node.left:
            queue.append(node.left)
            li.append(node.left.val)
        else:
            li.append(None)
        if node.right:
            queue.append(node.right)
            li.append(node.right.val)
        else:
            li.append(None)

    # 删掉末尾的null
    i = len(li) - 1
    while i > 0:
        if li[i] is None:
            del li[i]
        else:
            break
        i -= 1
    return li


s = Solution()
null = None
print(s.isValidBST(fromList([3, 1, 5, 0, 2, 4, 6])))
print(s.isValidBST(fromList([2, 1, 3])))
print(s.isValidBST(fromList([5, 4, 6, null, null, 3, 7])))
print(s.isValidBST(fromList([5, 1, 4, null, null, 3, 6])))

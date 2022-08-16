'''
652. 寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：后序遍历树
设数组allTree保存所有遍历过的树，数组dupliTree与allTree同样大小，dupliTree[i]表示allTree[i]是否为重复子树
后序遍历树，当前节点与allTree中以往保存的所有非重复子树进行对比，如果是重复子树，将其加入结果list，同时dupliTree[i]设置为true

时间复杂度：O(n^3)
空间复杂度：O(n)
'''


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def isSame(t1, t2):
            if t1.val != t2.val:
                return False
            if t1.left and t2.left:
                if not isSame(t1.left, t2.left):
                    return False
            elif t1.left or t2.left:
                return False
            if t1.right and t2.right:
                if not isSame(t1.right, t2.right):
                    return False
            elif t1.right or t2.right:
                return False
            return True

        treeNodeCount = []  # 保存各个子树的节点数
        allTree, dupliTree = [], []
        ans = []

        def postOrder(node):
            nodeCount = 1
            if node.left:
                nodeCount += postOrder(node.left)
            if node.right:
                nodeCount += postOrder(node.right)
            for i in range(len(allTree)):  # 与以往保存的所有子树进行对比
                if not dupliTree[i]:
                    if nodeCount == treeNodeCount[i] and isSame(allTree[i], node):  # 如果子树相同，保存到结果中
                        ans.append(node)
                        dupliTree[i] = True
                        break
            else:
                allTree.append(node)
                dupliTree.append(False)
                treeNodeCount.append(nodeCount)
            return nodeCount  # 返回子树节点数

        postOrder(root)
        return ans


null = None
tree = [1, 2, 3, 4, null, 2, 4, null, null, 4]


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
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
print(s.findDuplicateSubtrees(fromList(tree)))

'''
在二叉树中增加一行
给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。

添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。

将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。

如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。

示例 1:

输入:
二叉树如下所示:
       4
     /   \\
    2     6
   / \\   /
  3   1 5

v = 1

d = 2

输出:
       4
      / \\
     1   1
    /     \\
   2       6
  / \\     /
 3   1   5

示例 2:

输入:
二叉树如下所示:
      4
     /
    2
   / \\
  3   1

v = 1

d = 3

输出:
      4
     /
    2
   / \\
  1   1
 /     \\
3       1
注意:

输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。
输入的二叉树至少有一个节点。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：BFS
层序遍历每层节点，当遇到d-1层时，停止遍历，将队列中的d-1层节点的子节点前插入值为val的新节点

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        curD = 0
        dummyRoot = TreeNode(0, left=root)  # 设置一个哨兵根节点，简化算法
        q, nextq = [], []
        q.append(dummyRoot)
        while curD < depth - 1:
            node = q.pop()
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
            if not q:
                q, nextq = nextq, q
                curD += 1
        # 在d-1层的节点后面插入新的节点
        for node in q:
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)
        return dummyRoot.left


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
print(toList(s.addOneRow(fromList([1, 2, 3, 4]), 5, 4)))

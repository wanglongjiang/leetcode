'''
二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。


提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：迭代下降。
节点node如果只有左节点，左节点交换到右节点上。
    如果只有右节点，不需要处理
    如果左右都有节点，将左节点放到右边，右节点下降到左节点的最右子树。
    完成上面操作后，当前节点下降到右边节点。重复上面的处理
'''


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        while root.left or root.right:
            if root.left and root.right:
                right = root.right
                root.right = root.left  # left放到right
                root.left = None
                node = root.right
                while node.right:  # 原right节点放到新right的最右叶子节点上
                    node = node.right
                node.right = right
            elif root.left:
                root.right = root.left
                root.left = None
            root = root.right


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
t = fromList([1, 2, 5, 3, 4, null, 6])
s.flatten(t)
print(toList(t))
t = fromList([])
s.flatten(t)
print(toList(t))
t = fromList([0])
s.flatten(t)
print(toList(t))

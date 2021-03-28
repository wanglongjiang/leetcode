'''
二叉搜索树迭代器
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：使用中序遍历二叉树。
使用栈维护运行现场，先将左边节点全部入栈，每次next返回栈顶元素，如果栈顶元素有右节点，需要将右节点及其左子树入栈。
时间复杂度：O(n)
空间复杂度：O(h)，树的最大高度为h=logn
'''


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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
t = fromList([7, 3, 15, null, null, 9, 20])
iterator = BSTIterator(t)
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())

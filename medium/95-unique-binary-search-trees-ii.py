'''
不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：分治
以整数区间a..b中每一个元组作为子树的根节点，另外的元素作为左右子树，
递归生成左右子树的后，根节点与左右子树进行组合

时间复杂度：x， O(2^n)< x <O(n!)
空间复杂度：O(n)，最大递归深度n
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def makeTree(start, end):
            ans = []
            for i in range(start, end):
                leftTrees, rightTrees = [None], [None]
                if i > start:
                    leftTrees = makeTree(start, i)
                if i < end - 1:
                    rightTrees = makeTree(i + 1, end)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        node = TreeNode(i, leftTree, rightTree)
                        ans.append(node)
            return ans

        return makeTree(1, n + 1)


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
li = s.generateTrees(4)
for tree in li:
    print(toList(tree))

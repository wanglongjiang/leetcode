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
思路：回溯。
与96题类似，二叉搜索树的性质：根节点为root，所有的左子树节点小于root，所有的右子树节点大于root，其左右子树节点也满足这一性质。
根据这一特性，对于二叉搜索树nums[1..n]，如果第i个数为根节点，则nums[1..i-1]为左子树，nums[i+1..n]为右子树，再递归求左右子树
服用96题的回溯算法，另外设置2个数组left[1..n]和right[1..n]，分别代表节点1..n的左右子树用于输出
时间复杂度：x， O(2^n)< x <O(n!)
空间复杂度：O(n)，最大递归深度n，还需要3个大小为n的辅助空间
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        left, right = [0] * (n + 1), [0] * (n + 1)  # 这2个数组用于储存各个节点的左右子节点
        parentOk = set()
        trees = []

        def backtrack(parent, start, end):
            for i in range(start, end + 1):
                for j in filter(lambda x: x in parentOk, range(start, end + 1)):  # 子树发生变动，将子树节点的父节点清空，变成待赋值状态
                    parentOk.remove(j)
                left[i] = 0
                right[i] = 0
                if parent > i:  # 设置父节点的分支，若当前节点小于父节点，当前节点为父节点的左节点，否则为右节点
                    left[parent] = i
                else:
                    right[parent] = i
                parentOk.add(i)
                if len(parentOk) == n:  # 所有的节点都有父节点，是一颗完整的树，可以输出
                    output()
                if i - start >= 1:
                    backtrack(i, start, i - 1)
                if end - i >= 1:
                    backtrack(i, i + 1, end)

        def output():  # 输出树
            nodes = [TreeNode(val=i) for i in range(n + 1)]
            for i in range(1, n + 1):
                if left[i]:
                    nodes[i].left = nodes[left[i]]
                if right[i]:
                    nodes[i].right = nodes[right[i]]
            trees.append(nodes[right[0]])

        backtrack(0, 1, n)
        return trees


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
li = s.generateTrees(3)
for tree in li:
    print(toList(tree))

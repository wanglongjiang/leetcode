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
思路：迭代，回溯算法会导致部分左子树丢失。
二叉搜索树的性质：根节点为root，所有的左子树节点小于root，所有的右子树节点大于root，其左右子树节点也满足这一性质。
根据这一特性，对于二叉搜索树nums[1..n]，如果第i个数为根节点，则nums[1..i-1]为左子树，nums[i+1..n]为右子树，再递归求左右子树
另外设置2个数组left[1..n]和right[1..n]，分别代表节点1..n的左右子树用于输出
时间复杂度：x， O(2^n)< x <O(n!)
空间复杂度：O(n)，最大递归深度n，还需要3个大小为n的辅助空间
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nodes = [None] * (n + 1)
        trees = []
        # 创建所有节点，并连结成第1个树。第0个节点为哨兵
        for i in range(n + 1):
            nodes[i] = TreeNode(i + 1)
        for i in range(n):
            nodes[i].right = nodes[i + 1]
        # 尝试旋转所有子树

        def clone():  # 克隆并复制树
            newnodes = [TreeNode(val=i) for i in range(n + 1)]
            for i in range(1, n + 1):
                if nodes[i].left:
                    newnodes[i].left = newnodes[nodes[i].left.val]
                if nodes[i].right:
                    newnodes[i].right = nodes[nodes[i].right.val]
            trees.append(newnodes[0].right)

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
li = s.generateTrees(4)
for tree in li:
    print(toList(tree))

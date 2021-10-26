'''
二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：动态规划。
该题目具有典型的最优子结构。
1、叶子节点的最大路径和为val
2、非叶子节点，经过它的的最大路径和为val+min(0,左子树的最大路径和)+min(0,右子树的最大路径和)
首先计算所有叶子节点的最大路径和，然后计算上级节点的路径和。
1、层遍历所有节点，加入二维数组。
2、从最下面一层节点开始计算其最大路径和，放入哈希表中。
    如果是叶子节点，pathSum[node] = node.val
    如果不是叶子节点，pathSum[node] = max(leftsum, rightsum) + node.val
所有的节点的最大路径和中的最大值即为返回值
时间复杂度：O(n)，需要遍历2次节点
空间复杂度：O(n)，遍历和动态规划哈希表都需要O(n)空间
'''


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        nodes = [[]]
        # bfs遍历所有节点
        queue = [root, None]
        while queue:
            node = queue[0]
            del queue[0]
            if not node:
                if not queue or not queue[-1]:  # 如果队列中最后一个节点为null，说明没有需要遍历的
                    continue
                queue.append(node)
                nodes.append([])
                continue
            nodes[-1].append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 从最下面一层开始，依次计算所有节点的最大路径和
        pathSums = {}
        maxSum = float('-inf')
        while nodes:
            layer = nodes.pop()
            for node in layer:
                leftsum, rightsum = 0, 0
                if node.left and pathSums[id(node.left)] > 0:  # 只有大于0才合计
                    leftsum = pathSums[id(node.left)]
                if node.right and pathSums[id(node.right)] > 0:
                    rightsum = pathSums[id(node.right)]
                pathSums[id(node)] = max(leftsum, rightsum) + node.val
                maxSum = max(maxSum, leftsum + rightsum + node.val)
        return maxSum


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


s = Solution()
null = None
print(s.maxPathSum(fromList([1, 2, 3])))
print(s.maxPathSum(fromList([-10, 9, 20, null, null, 15, 7])))
print(s.maxPathSum(TreeNode(-3)))
print(s.maxPathSum(fromList([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1])))

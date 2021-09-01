'''
剑指 Offer 32 - II. 从上到下打印二叉树 II

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：BFS遍历树
广度优先遍历树
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        from collections import deque
        q = deque()
        q.append(root)
        nextq = deque()
        while q or nextq:
            if not q:  # 当前队列为空时，将下一队列改成当前队列，下一队列清空
                q, nextq = nextq, q
                ans.append([])
                continue
            node = q.popleft()
            ans[-1].append(node.val)
            if node.left:
                nextq.append(node.left)
            if node.right:
                nextq.append(node.right)
        return ans

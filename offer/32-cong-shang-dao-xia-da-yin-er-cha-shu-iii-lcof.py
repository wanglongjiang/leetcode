'''
剑指 Offer 32 - III. 从上到下打印二叉树 III

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推。
提示：

节点总数 <= 1000
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
广度优先遍历树，结果中的奇数行倒序
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]]
        if not root:
            return ans
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
        # 倒序处理
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans

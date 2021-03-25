'''
二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：按照BFS遍历树
按照BFS遍历树，然后结果中奇数层数组需要逆序。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        ans.append([])
        queue = [root, None]
        i = 0
        # 遍历树，层序输出到结果中
        while i < len(queue):
            node = queue[i]
            i += 1
            if not node:
                queue.append(None)
                if queue[len(queue) - 2] is None:  # 最后2个都是None，说明队列中没有需要处理的节点，退出循环
                    break
                ans.append([])
                continue
            ans[len(ans) - 1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 颠倒奇数层的结果
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans


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


s = Solution()
null = None
print(s.zigzagLevelOrder(fromList([1, 2, 3, 4, null, null, 5])))
print(s.zigzagLevelOrder(fromList([3, 9, 20, null, null, 15, 7])))

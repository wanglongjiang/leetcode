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
需要设置1个二维队列辅助，奇数层遍历时按照队列方式FIFO，偶数层遍历按照堆栈方式LIFO
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]]
        if not root:
            return ans
        queue = [[root], []]
        while len(queue) > 1 or len(queue[0]) > 0:
            if len(ans) % 2 == 1:  # 单数排，从左到右出队列
                node = queue[0][0]
                del queue[0][0]
            else:  # 偶数排，先入先出栈
                node = queue[0].pop()
            ans[len(ans) - 1].append(node.val)
            if node.left:
                queue[len(queue) - 1].append(node.left)
            if node.right:
                queue[len(queue) - 1].append(node.right)
            if len(queue[0]) == 0:
                del queue[0]
                if len(queue[0]) > 0:
                    queue.append([])
                    ans.append([])
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
print(s.zigzagLevelOrder(fromList([3, 9, 20, null, null, 15, 7])))

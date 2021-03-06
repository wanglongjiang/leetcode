'''
二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：按照BFS遍历树
需要设置1个队列辅助，每层结束时，向辅助队列里插入null元素标志着一层的结束
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]]
        if not root:
            return ans
        queue = [root, None]  # 每层结束，后面插入一个null作为分隔符
        while len(queue) > 0:
            node = queue[0]
            del queue[0]
            if not node:
                if len(queue) > 0:  # 遇到分层分割，重新新起一行
                    queue.append(None)
                    ans.append([])
            else:
                ans[len(ans) - 1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
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
print(s.levelOrder(fromList([3, 9, 20, null, null, 15, 7])))

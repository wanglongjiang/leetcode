'''
314. 二叉树的垂直遍历
给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。

如果两个结点在同一行和列，那么顺序则为 从左到右。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
示例 2：


输入：root = [3,9,8,4,0,1,7]
输出：[[4],[9],[3,0,1],[8],[7]]
示例 3：


输入：root = [3,9,8,4,0,1,7,null,null,null,2,5]
输出：[[4],[9,5],[3,0,1],[8,2],[7]]
示例 4：

输入：root = []
输出：[]


提示：

树中结点的数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''

from typing import List
from collections import defaultdict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：哈希 BFS
设哈希表，key为列号，val为list。
根节点列号初始设为0，左子树列号-1，右子树列号+1。
BFS遍历树，确保节点从上到下，从左到右被遍历。对于当前节点，在哈希表中用列号找到list，然后添加到list中，确保按照正确的列号被访问。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        hashtab = defaultdict(list)

        q, nextq = deque(), deque()
        q.append((root, 0))
        while q:
            node, col = q.popleft()
            hashtab[col].append(node.val)  # 将节点值按照列的索引找到list，添加到list中
            if node.left:
                nextq.append((node.left, col - 1))
            if node.right:
                nextq.append((node.right, col + 1))
            if not q:
                q, nextq = nextq, q

        ans = []
        for col in sorted(hashtab.keys()):  # 按照列索引，从左到右输出
            ans.append(hashtab[col])
        return ans


null = None


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
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i] is not None:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
print(s.verticalOrder(fromList([3, 9, 8, 4, 0, 1, 7])))
print(s.verticalOrder(fromList([3, 9, 20, null, null, 15, 7])))
print(s.verticalOrder(fromList([3, 9, 8, 4, 0, 1, 7, null, null, null, 2, 5])))
print(s.verticalOrder(fromList([])))

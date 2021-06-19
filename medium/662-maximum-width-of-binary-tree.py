'''
二叉树最大宽度

给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。
这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
按照堆的方式给节点编号，根节点为0，它的2个节点编号分别为1、2，也即为节点i的左右子节点为2i+1和2i+2
DFS遍历树，对于每层节点，记录编号最大的节点和最小的节点
遍历完成后，用每层的最大编号减去最小编号，得到每层的宽度，找到最大宽度即可

时间复杂度：O(n)，n为节点数
空间复杂度：O(h),h为树的高度
'''


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        minList, maxList = [], []

        def dfs(node, nodeNo, depth):
            if len(minList) < depth + 1:
                minList.append(float('inf'))
                maxList.append(float('-inf'))
            minList[depth] = min(minList[depth], nodeNo)  # 设置该层最小节点编号
            maxList[depth] = max(maxList[depth], nodeNo)  # 设置该层最大节点编号
            if node.left:
                dfs(node.left, 2 * nodeNo + 1, depth + 1)  # 下层左节点编号为当前节点2*i+1
            if node.right:
                dfs(node.right, 2 * nodeNo + 2, depth + 1)  # 下层右节点编号为当前节点2*i+2

        dfs(root, 0, 0)
        return max(map(lambda x: x[1] - x[0] + 1, zip(minList, maxList)))


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
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


null = None
s = Solution()
print(s.widthOfBinaryTree(fromList([1, 3, 2, 5, 3, null, 9])))

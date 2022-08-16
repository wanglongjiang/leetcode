'''
1080. 根到叶路径上的不足节点
给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。

请你删除所有不足节点，并返回生成的二叉树的根。



示例 1：


输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

输出：[1,2,3,4,null,null,7,8,9,null,14]
示例 2：


输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

输出：[5,4,8,11,null,17,4,7,null,null,null,5]
示例 3：


输入：root = [5,-6,-6], limit = 0
输出：[]


提示：

给定的树有 1 到 5000 个节点
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：dfs
递归遍历所有节点，将祖先节点的值累加到当前节点上，再传递给左右子节点。
如果当前节点是叶子节点，将合计后的累计值传递给父节点。
如果当前节点不是叶子节点，判断子树的累计值是否<limit，如果小于，删除子树。

时间复杂度：O(n)
空间复杂度：O(h)
'''


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, s):
            s += node.val
            childVal = float('-inf')
            if node.left:
                leftVal = dfs(node.left, s)
                if leftVal < limit:
                    node.left = None
                childVal = max(childVal, leftVal)
            if node.right:
                rightVal = dfs(node.right, s)
                if rightVal < limit:
                    node.right = None
                childVal = max(childVal, rightVal)
            return childVal if childVal != float('-inf') else s

        if not root:
            return root
        if dfs(root, 0) < limit:
            return None
        return root


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
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


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
print(toList(s.sufficientSubset(fromList([1, 2, -3, -5, null, 4, null]), -1)))

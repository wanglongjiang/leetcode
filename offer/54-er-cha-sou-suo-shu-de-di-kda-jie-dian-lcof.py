'''
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \\
 1   4
  \\
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \\
     3   6
    / \\
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
思路：DFS
先右子树，
> 如果k>右子树节点数，则k-=右子树
> 如果k<=右子树节点数，已经找到了，不需要继续遍历，返回

然后本节点
> k-=1
> 如果k==0, 当前节点即为结果，返回

最后遍历左子树，返回当前节点为根的树的节点数

时间复杂度：O(k)
空间复杂度：O(h)
'''


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        ans = 0

        def dfs(node, k):
            nonlocal ans
            rightSize, leftSize = 0, 0
            if node.right:
                rightSize = dfs(node.right, k)
                k -= rightSize  # 减去右子树
                if k <= 0:
                    return rightSize
            k -= 1  # 减去当前节点
            if k == 0:  # 如果k变成0，当前节点就是第k大的节点
                ans = node.val
                return rightSize + 1
            if node.left:
                leftSize = dfs(node.left, k)
            return rightSize + 1 + leftSize

        dfs(root, k)
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
print(
    s.kthLargest(
        fromList([
            41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, null, 43, 46, 49, 0, 2, 30, 36, null, null, null, null, null, null, 45, 47, null, null, null, null, null,
            4, 29, 32, null, null, null, null, null, null, 3, 9, 26, null, 31, 34, null, null, 7, 11, 25, 27, null, null, 33, null, 6, 8, 10, 16, null, null,
            null, 28, null, null, 5, null, null, null, null, null, 15, 19, null, null, null, null, 12, null, 18, 20, null, 13, 17, null, null, 22, null, 14,
            null, null, 21, 23
        ]), 25))
print(s.kthLargest(fromList([5, 3, 6, 2, 4, null, null, 1]), 3))

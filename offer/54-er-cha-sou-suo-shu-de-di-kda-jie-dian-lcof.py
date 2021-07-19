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
> 如果k>右子树，则k-=右子树
> 如果k<=右子树，已经找到了，不需要继续遍历，返回
然后本节点
> 如果k>1，k-=1
> 如果k==1, 当前节点即为结果，返回
然后遍历左子树

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
                if k <= rightSize:
                    return rightSize
                else:
                    k -= rightSize
            if k > 1:
                k -= 1
            else:
                ans = node.val
                return rightSize + 1
            if node.left:
                leftSize = dfs(node.left, k)
                if k <= leftSize:
                    return leftSize
                else:
                    k -= leftSize
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
print(s.kthLargest(fromList([5, 3, 6, 2, 4, null, null, 1]), 3))

'''
1382. 将二叉搜索树变平衡
给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

 

示例 1：



输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
示例 2：



输入: root = [2,1,3]
输出: [2,1,3]
 

提示：

树节点的数目在 [1, 104] 范围内。
1 <= Node.val <= 105
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：分治
1、按照二叉搜索树的性质，从左到右遍历所有子树，将记录提取到数组中
2、按照分治法，将数组递归切分成2份，生成新的二叉搜索树

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 读取所有节点
        def read(node, arr):
            if node.left:
                read(node.left, arr)
            arr.append(node.val)
            if node.right:
                read(node.right, arr)

        arr = []
        read(root, arr)

        # 用分治法重构平衡二叉搜索树
        def write(arr, start, end):
            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            if mid > start:
                node.left = write(arr, start, mid)
            if end > mid + 1:
                node.right = write(arr, mid + 1, end)
            return node

        return write(arr, 0, len(arr))


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
print(s.balanceBST(fromList([2, 1, 3])))

'''
两棵二叉搜索树中的所有元素

给你 root1 和 root2 这两棵二叉搜索树。

请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：

输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]
示例 3：

输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]
示例 4：

输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]
示例 5：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：树的遍历
因为搜索树已经有序，可以前序遍历2颗树，得到2个list，然后将2个list按照从小到大进行合并

时间复杂度：O(n+m),n、m分别为2个树的节点数
空间复杂度：O(n+m)
'''


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 前序遍历数，将数字提取到2个list中
        def preOrder(node, li):
            if node.left:
                preOrder(node.left, li)
            li.append(node.val)
            if node.right:
                preOrder(node.right, li)

        li1, li2 = [], []
        if root1:
            preOrder(root1, li1)
        if root2:
            preOrder(root2, li2)
        # 合并2个list
        m, n = len(li1), len(li2)
        ans = [0] * (m + n)
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if li1[i] <= li2[j]:
                ans[k] = li1[i]
                i += 1
            else:
                ans[k] = li2[j]
                j += 1
            k += 1
        while i < m:
            ans[k] = li1[i]
            k += 1
            i += 1
        while j < n:
            ans[k] = li2[j]
            k += 1
            j += 1
        return ans

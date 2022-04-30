'''
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2^h 个节点。



示例 1：

输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1


提示：

树中节点的数目范围是[0, 5 * 10^4]
0 <= Node.val <= 5 * 10^4
题目数据保证输入的树是 完全二叉树


进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：二分查找
首先遍历最左侧节点，计算出完全二叉树的高度h。
那么最底层的元素数最多有2^h个（从0开始），每个元素的编号为0..2^h-1。
可以用二分查找的方法，第一次查找2^(h-1)的节点，
如果该节点存在，则继续二分查找2^(h-1)..2^h之间的节点
如果该节点不存在，则继续二分查找0..2^(h-1)之间的节点
直至两个相邻的节点i存在，i+1不存在，那么返回2^h+i

时间复杂度：O(logn^2)
空间复杂度：O(logn)
'''


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        h = -1
        # 计算h
        node = root
        while node:
            h += 1
            node = node.left
        # 开始二分查找
        start, end = 0, (1 << h) - 1
        exists = {}
        while True:
            mid = (start + end) // 2
            node = root
            for i in range(h - 1, -1, -1):  # 向下查找序号是mid的节点是否存在
                if (1 << i) & mid:
                    node = node.right
                else:
                    node = node.left
            exists[mid] = node is not None  # 将mid是否存在记录到哈希表中
            if not node:
                if (mid - 1) in exists and exists[mid - 1]:  # mid-1存在，mid不存在，可以确定个数
                    return (1 << h) - 1 + mid
                end = mid - 1  # 不能确定个数，需要缩小二分查找的范围
            else:
                if mid == (1 << h) - 1:  # 如果是最后一个节点，且其存在，可以确定个数
                    return (1 << h) + mid
                if (mid + 1) in exists and not exists[mid + 1]:  # mid存在，mid+1不存在，可以确定个数
                    return (1 << h) + mid
                start = mid + 1  # 不能确定个数，需要缩小二分查找的范围


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


s = Solution()
print(s.countNodes(fromList([1])))
print(s.countNodes(fromList([1, 2])))
print(s.countNodes(fromList([1, 2, 3])))
print(s.countNodes(fromList([1, 2, 3, 4])))
print(s.countNodes(fromList([1, 2, 3, 4, 5])))
print(s.countNodes(fromList([1, 2, 3, 4, 5, 6])))
print(s.countNodes(fromList([1, 2, 3, 4, 5, 6, 7])))
print(s.countNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8])))
print(s.countNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(s.countNodes(fromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

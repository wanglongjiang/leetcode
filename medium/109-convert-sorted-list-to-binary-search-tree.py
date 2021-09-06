'''
有序链表转换二叉搜索树

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：分治
将链表转为list，然后用分治法递归下降分解list

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        li = []
        while head:
            li.append(head.val)
            head = head.next

        def dc(start, end):
            if start == end:
                return TreeNode(li[start])
            mid = (start + end) // 2
            node = TreeNode(li[mid])
            if mid > start:
                node.left = dc(start, mid - 1)
            if end > mid:
                node.right = dc(mid + 1, end)
            return node

        return dc(0, len(li) - 1)

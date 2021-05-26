'''
二叉树中的列表
给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。

一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

 

示例 1：



输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。
示例 2：



输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
示例 3：

输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。
 

提示：

二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
链表包含的节点数目在 1 到 100 之间。
二叉树包含的节点数目在 1 到 2500 之间。
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
思路：树 暴力搜索
从树的每一个节点出发，向下搜索有没有与链表相同的路径
2重递归：
1. 第1个递归函数是DFS遍历树
2. 第2个递归函数是查找是否有匹配链表的路径

时间复杂度：O(mn)
空间复杂度：O(h)
'''


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # 从指定节点向下搜索链表
        def hasMatch(treeNode, liNode):
            if treeNode.val == liNode.val:
                if liNode.next is None:
                    return True
                if treeNode.left:
                    if hasMatch(treeNode.left, liNode.next):
                        return True
                if treeNode.right:
                    if hasMatch(treeNode.right, liNode.next):
                        return True
            return False

        # 遍历树
        def dfs(treeNode):
            if treeNode.val == head.val:
                if hasMatch(treeNode, head):
                    return True
            else:
                if treeNode.left:
                    if dfs(treeNode.left):
                        return True
                if treeNode.right:
                    if dfs(treeNode.right):
                        return True
            return False

        return dfs(root)

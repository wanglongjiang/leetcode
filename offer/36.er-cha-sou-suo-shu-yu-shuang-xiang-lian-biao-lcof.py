'''
剑指 Offer 36. 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。


为了让您更好地理解问题，以下面的二叉搜索树为例：


我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。


特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
还需要返回链表中的第一个节点的指针。

 

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。
'''
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：分治
将整棵树分解成左子树转成的leftList，右子树转成的rightList，当前节点的前驱是leftList,后驱是rightList。
如果当前节点没有子节点，需要将接的前驱、后驱都设置成自身
如果当前节点有左树，将左树的最后一个节点（首节点的前驱）设置为当前节点，当前节点设置为其后驱，当前节点的后驱为左树的首节点，左树的首节点前驱设置为当前节点
如果当前节点有右树，将2个链表连结。

时间复杂度：O(n)
空间复杂度：O(k)，k是树的深度
'''


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if not root.left and not root.right:  # 没有子节点，将前后驱指向自身，返回
            root.left = root
            root.right = root
            return root
        head = root
        right = root.right
        if root.left:  # 分治处理左子树
            head = self.treeToDoublyList(root.left)  # 得到左子树头节点
            tail = head.left  # 左子树最后一个节点
            # 将当前节点与左子树形成的链表连结到一起
            head.left = root
            root.right = head
            tail.right = root
            root.left = tail
        if right:  # 分治处理右子树
            rhead = self.treeToDoublyList(right)
            rtail = rhead.left
            rhead.left = root
            root.right = rhead
            rtail.right = head
            head.left = rtail
        return head


def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = Node(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = Node(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = Node(val=li[i])
                queue.append(node.right)
            i += 1
    return root


s = Solution()
node = s.treeToDoublyList(fromList([4, 2, 5, 1, 3]))
print(node)

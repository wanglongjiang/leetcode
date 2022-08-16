'''
426. 将二叉搜索树转化为排序的双向链表
将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。



示例 1：

输入：root = [4,2,5,1,3]


输出：[1,2,3,4,5]

解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。

示例 2：

输入：root = [2,1,3]
输出：[1,2,3]
示例 3：

输入：root = []
输出：[]
解释：输入是空树，所以输出也是空链表。
示例 4：

输入：root = [1]
输出：[1]


提示：

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
Node.val 的所有值都是独一无二的
0 <= Number of Nodes <= 2000
'''


# Definition for a Node.
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

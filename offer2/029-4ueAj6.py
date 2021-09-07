'''
剑指 Offer II 029. 排序的循环链表
给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

 

示例 1：


 

输入：head = [3,4,1], insertVal = 2
输出：[3,4,1,2]
解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。
新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。


示例 2：

输入：head = [], insertVal = 1
输出：[1]
解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。
示例 3：

输入：head = [1], insertVal = 0
输出：[1,0]
 

提示：

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
 

注意：本题与主站 708 题相同： https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4ueAj6
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


'''
思路：链表的遍历
沿着head向前遍历节点，设当前节点为node，遍历过程中记录最大节点maxNode：
> 如果node.val== insertVal，则将node插入node后面
> 如果node.val<insertVal, node.next.val>=insertVal，将node插入node后面
链表完全遍历一次后，如果未找到满足上面条件，说明insertVal超过最大值或小于最小值，这种情况下将insertVal插入到maxNode后面。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)
        if not head:
            insertNode.next = insertNode
            return insertNode
        node, maxNode = head, head
        while True:
            if maxNode.val <= node.val:
                maxNode = node
            if insertVal == node.val or node.val < insertVal <= node.next.val:  # 找到合适的插入位置，插入后返回
                insertNode.next = node.next
                node.next = insertNode
                return head
            node = node.next
            if node == head:  # 遍历了一圈，未找到插入位置，退出
                break
        insertNode.next = maxNode.next  # 插入到最大和最小值之间
        maxNode.next = insertNode
        return head


def fromList(li: List[int]):
    head = None
    tail = head
    for item in li:
        if head is None:
            head = Node(item)
            tail = head
        else:
            tail.next = Node(item)
            tail = tail.next
    return head


s = Solution()

a1 = Node(1)
a1.next = a1
print(s.insert(a1, 0))

a1 = Node(1)
a3 = Node(3)
a4 = Node(4)
a1.next = a3
a3.next = a4
a4.next = a1

print(s.insert(a3, insertVal=2))

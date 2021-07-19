'''
设计链表
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3
 

提示：

所有val值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：设计 链表
数据量较小，老老实实写链表

时间复杂度：get、addAtIndex、deleteAtIndex均为O(n)，addAtHead、addAtTail为O(1)
'''


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.n = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.n:
            i = 0
            node = self.head.next
            while i < index:
                node = node.next
                i += 1
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        self.n += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self.n:
            return
        i = 0
        node = self.head.next
        while i < index:
            node = node.next
            i += 1
        newnode = Node(val)
        newnode.next = node
        newnode.prev = node.prev
        node.prev = newnode
        newnode.prev.next = newnode
        self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.n:
            i = 0
            node = self.head.next
            while i < index:
                node = node.next
                i += 1
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            node.prev = None
            node.next = None
            self.n -= 1

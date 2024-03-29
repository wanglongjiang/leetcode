class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fromList(li: int):
    head = None
    tail = head
    for item in li:
        if head is None:
            head = ListNode(item)
            tail = head
        else:
            tail.next = ListNode(item)
            tail = tail.next
    return head


def toList(listNode: ListNode):
    if listNode is None:
        return []
    else:
        li = []
        while listNode is not None:
            li.append(listNode.val)
            listNode = listNode.next
        return li


def rev(headB):
    newHead = None
    lenB = 0
    next = headB
    while next:
        lenB += 1
        nextnext = next.next
        next.next = newHead
        newHead = next
        next = nextnext
    print(lenB)
    return newHead

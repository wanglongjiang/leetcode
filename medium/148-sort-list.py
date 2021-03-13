'''
排序链表

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
'''

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路，自底向上的归并排序
题目中没有指出O(nlogn)是在平均情况下还是最坏情况下，最坏情况下能达到O(nlogn)的排序算法有归并排序、堆排序、基数排序。
其他的排序如选择、冒泡、插入、快排、希尔等达不到这个要求。
这里的数据结构是链表，堆排序不适用，基数排序也不适用。只能采用归并排序。

常规归并排序的空间复杂度是O(n)，想了1个自底向上的归并排序算法：
第1次遍历，每2个元素为1组，进行组内排序。
第2次遍历，每4个元素为1组，它的左右2部分已经排序完成，2个部分依次比较、交换
第3次遍历，每8个元素为1组，它的左右2部分已经排序完成，。。。
经过logn次遍历，链表变为有序。

还未完成。。。

时间复杂度：O(nlogn)，需要经过logn次遍历
空间复杂度：O(1)
'''


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        subLen, n = 1, 0
        p = head
        while p:  # 先遍历一遍求出n
            p = p.next
            n += 1
        head = ListNode(0, head)  # 设置1个假头，简化算法
        while subLen < n:
            right = head.next
            preRight = head
            preLeft = head
            # 每个循环right指针前进2*subLen，合并2*subLen长度的链表
            while right:
                left = right  #
                i = 0
                while i < subLen and right:  # 定位right指针
                    right = right.next
                    i += 1
                if not right:
                    break
                leftIndex, rightIndex = 0, 0
                # 2个有序链表按照大小合并
                while left and right and leftIndex < subLen and rightIndex < subLen:
                    if left.next.val > right.next.val:  # 左边大于右边，将右边的节点插入左边
                        rightNext = right.next
                        right.next = rightNext.next
                        rightNext.next = left.next
                        left.next = rightNext
                        left = left.next
                        right = right.next
                        rightIndex += 1
                    else:
                        leftIndex += 1
                        left = left.next
                while right and rightIndex < subLen:
                    right = right.next
                    rightIndex += 1
            subLen *= 2
        return head.next


def fromList(li: List[int]):
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


s = Solution()
print(toList(s.sortList(fromList([]))))
print(toList(s.sortList(fromList([1]))))
print(toList(s.sortList(fromList([2, 1]))))
print(toList(s.sortList(fromList([3, 2, 1]))))
print(toList(s.sortList(fromList([4, 2, 1, 3]))))
print(toList(s.sortList(fromList([-1, 5, 3, 4, 0]))))

'''
分隔链表
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]

示例 1：

输入:
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。
例如, 输入的结点 root 的 val= 1, root.next.val = 2, root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
示例 2：

输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释:
输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
 

提示:

root 的长度范围： [0, 1000].
输入的每个节点的大小范围：[0, 999].
k 的取值范围： [1, 50].
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表
首先遍历依次链表，求其总长度totalSize，然后除以k，得到其平均长度size和余数remainder。
然后再次遍历链表，每次切割size个(余数=0)或size+1个（余数>0)，设置到结果中

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        totalSize = 0
        node = root
        # 统计总长度
        while node:
            totalSize += 1
            node = node.next
        # 求平均长度，余数
        size, remainder = divmod(totalSize, k)
        ans = []
        # 分割链表
        head = root
        node = root
        needSize = size + (1 if remainder else 0)
        if remainder > 0:
            remainder -= 1
        while node:
            needSize -= 1
            if needSize == 0:  # 已经凑够了子数组大小，从原数组裁剪掉，写入结果
                nextNode = node.next
                node.next = None
                ans.append(head)
                head = nextNode
                node = nextNode
                needSize = size + (1 if remainder else 0)  # 计算下一个子数组大小
                if remainder > 0:
                    remainder -= 1
            else:
                node = node.next
        while len(ans) < k:  # 如果分割的个数不够k个，用空链表补足
            ans.append(None)
        return ans

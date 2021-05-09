'''
链表中的下一个更大节点

给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。

每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.val，
那么就有 j > i 且  node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0 。

返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。

注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，
第三个节点值为 5 。

 

示例 1：

输入：[2,1,5]
输出：[5,5,0]
示例 2：

输入：[2,7,4,3,5]
输出：[7,0,5,5,0]
示例 3：

输入：[1,7,5,1,9,2,5,1]
输出：[7,9,9,9,0,5,0,0]
 

提示：

对于链表中的每个节点，1 <= node.val <= 10^9
给定列表的长度在 [0, 10000] 范围内
'''
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：单调栈
主要思路：典型的需要用栈解决的问题。
当遍历链表时，第i个节点，无法确定它的更大值，只能保存到栈中，等遍历到后面的元素node[j].val>node[i].val时才有更大值。
因为遍历到j的时候，栈中单调元素递减，所以栈中[i..j-1]都会小于node[j].val，它们的更大值都是node[j].val。具体算法如下：
依次遍历链表，
    1、如果当前元素val<=栈顶元素或者栈为空，需要入栈，当前元素的更大值暂时设置为0。
    2、如果当前元素大于栈顶元素，栈顶元素的更大值为当前元素，需要将栈顶出栈，当前元素作为栈顶元素的更大值输出到结果数组中。
    持续上面的过程2，直至栈为空或者当前元素<=栈顶元素，最后将当前元素入栈。
最后栈内剩余的元素都是找不到更大值，设置为0.
时间复杂度：O(n)，每个元素最多入栈1次
空间复杂度：O(n)，需要栈空间存放值和索引
'''


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        vstack = []  # 存放值
        istack = []  # 存放索引
        ans = []
        i = 0
        while head:
            ans.append(0)
            while vstack and head.val > vstack[-1]:
                ans[istack.pop()] = head.val
                vstack.pop()
            vstack.append(head.val)
            istack.append(i)
            i += 1
            head = head.next
        return ans


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


s = Solution()
print(s.nextLargerNodes(fromList([2, 1, 5])))

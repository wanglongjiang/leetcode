'''
剑指 Offer II 078. 合并排序链表
给定一个链表数组，每个链表都已经按升序排列。

请将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
 

注意：本题与主站 23 题相同： https://leetcode-cn.com/problems/merge-k-sorted-lists/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/vvXgSW
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：分治，归并
如果list的大小为1或0，直接返回链表，
如果list的大小>1，将list递归分成2部分，再分别针对这2部分进行递归的分治，然后将2个分治的子过程返回的链表进行归并

时间复杂度：O(nlogn)
空间复杂度：O(logn)
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(start, end) -> ListNode:
            if end - start == 0:
                return None
            elif end - start == 1:
                return lists[start]
            else:
                mid = (start + end) // 2
                li1 = merge(start, mid)
                li2 = merge(mid, end)
                newlist = None
                tail = None
                while li1 is not None and li2 is not None:
                    if li1.val <= li2.val:
                        smallNode = li1
                        li1 = li1.next
                    else:
                        smallNode = li2
                        li2 = li2.next
                    if newlist is None:
                        newlist = ListNode(smallNode.val)
                        tail = newlist
                    else:
                        tail.next = ListNode(smallNode.val)
                        tail = tail.next
                if newlist is None:
                    newlist = li1 if li2 is None else li2
                else:
                    tail.next = li1 if li2 is None else li2
                return newlist

        return merge(0, len(lists))

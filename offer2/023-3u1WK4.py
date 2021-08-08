'''
剑指 Offer II 023. 两个链表的第一个重合节点
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：



题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
 

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]
 

进阶：能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3u1WK4
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
思路：链表反转。将其中一个链表反转后，如果从另外一个链表出发，能到达另外反转后的的链表表尾（原表头），如果不能到达，则没有相交。
1、链表a遍历一次到最后，算出a的长度lenA
2、链表b进行反转，同时技术出b的长度lenB
3、然后从a再出发，算出新的长度lenC。
4、将b反转，恢复原状。
我们把相交点设为i，从相交点之后的长度2个链表相同均为c，
A相交点前面的长度为a，B相交点前面的长度为b，有下面的3元一次方程：
lenA=a+c，lenB=b+c，lenC=a+b+1
求解方程后得到
a=(lenc-lenb+lena-1)/2
5、从a出发，第a+1个元素即为相交点
PS. 官方题解使用双指针，只需要遍历2次，且没有修改

时间复杂度：O(n)，4.X次遍历
空间复杂度：O(1)
'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB, lenC = 0, 0, 0
        # 1、遍历A求lenA
        node = headA
        while node:
            lenA += 1
            node = node.next
        # 2、翻转B，同时求lenB
        newHead = None
        next = headB
        while next:
            lenB += 1
            nextnext = next.next
            next.next = newHead
            newHead = next
            next = nextnext
        # 3、遍历A，求lenC，判断是否相交
        node = headA
        isIntersect = False
        while node:
            lenC += 1
            if node == headB:
                isIntersect = True
            node = node.next
        # 4、翻转B，恢复原状
        next = newHead
        newHead = None
        while next:
            nextnext = next.next
            next.next = newHead
            newHead = next
            next = nextnext
        if not isIntersect:  # 没有相交，返回null
            return None
        # 5、遍历A，取第a个节点，即为相交点
        a = (lenC - lenB + lenA - 1) // 2
        while headA:
            if a == 0:
                return headA
            a -= 1
            headA = headA.next

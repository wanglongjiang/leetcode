'''
剑指 Offer 35. 复杂链表的复制

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
 

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/
'''


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


'''
思路：哈希表。用哈希表存放链表节点与索引之间的映射，第1次顺序访问原链表的过程创建新链表，将原链表节点放入哈希表，第2次遍历原链表，将random指针复制出来。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        newNodes = []
        oldNodeIndexMap = {}
        oldNode = head
        i = 0
        # 第1次遍历创建只有next指针赋值的链表
        while oldNode:
            oldNodeIndexMap[id(oldNode)] = i
            newNode = Node(oldNode.val)
            newNodes.append(newNode)
            if i:
                newNodes[i - 1].next = newNode
            i += 1
            oldNode = oldNode.next
        # 第2次遍历复制random指针
        while head:
            if head.random:
                i = oldNodeIndexMap[id(head)]
                randomIndex = oldNodeIndexMap[id(head.random)]
                newNodes[i].random = newNodes[randomIndex]
            head = head.next
        return newNodes[0]

'''
2326. 螺旋矩阵 IV
给你两个整数：m 和 n ，表示矩阵的维数。

另给你一个整数链表的头节点 head 。

请你生成一个大小为 m x n 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。
如果还存在剩余的空格，则用 -1 填充。

返回生成的矩阵。

 

示例 1：


输入：m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
输出：[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
解释：上图展示了链表中的整数在矩阵中是如何排布的。
注意，矩阵中剩下的空格用 -1 填充。
示例 2：


输入：m = 1, n = 4, head = [0,1,2]
输出：[[0,1,2,-1]]
解释：上图展示了链表中的整数在矩阵中是如何从左到右排布的。 
注意，矩阵中剩下的空格用 -1 填充。
 

提示：

1 <= m, n <= 105
1 <= m * n <= 105
链表中节点数目在范围 [1, m * n] 内
0 <= Node.val <= 1000
'''
import hmac
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
思路：模拟
模拟矩阵旋转方向依次填充

时间复杂度：O(m*n)
空间复杂度：O(1)
'''


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = [[-1] * n for _ in range(m)]
        i = j = di = 0
        while head:
            ans[i][j] = head.val
            head = head.next
            dx, dy = directs[di]
            if not (0 <= i + dx < m and 0 <= j + dy < n and ans[i + dx][j + dy] == -1):
                di = (di + 1) % 4
                dx, dy = directs[di]
            i += dx
            j += dy
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
print(s.spiralMatrix(10, 1, fromList([8, 24, 5, 21, 10, 11, 11, 12, 6, 17])))
print(s.spiralMatrix(m=3, n=5, head=fromList([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])))

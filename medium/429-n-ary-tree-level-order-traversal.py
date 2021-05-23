'''
N 叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

 

示例 1：

输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]

示例 2：

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

提示：

树的高度不会超过 1000
树的节点总数在 [0, 10^4] 之间
'''
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


'''
思路：树
用2个队列辅助，按层遍历。
设2个队列curQ,nextQ
1. 将根节点加入队列curQ
2. 从队列curQ中弹出一个节点，将其所有子节点加入下一层队列nextQ。
3. 如果curQ为空，将其与nextQ交换。这个时候说明该层的节点已全部收集完，需要把队列中的元素也输出到结果中。
4. 回到2，继续遍历队列，直至队列为空
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        curQ, nextQ = deque(), deque()
        curQ.append(root)
        while curQ:
            node = curQ.popleft()
            nextQ.extend(node.children)  # 子节点全部加入队列
            if not curQ:  # 当前层的队列遍历完毕，遍历下一层的队列
                curQ, nextQ = nextQ, curQ
                if curQ:  # 如果下一层有节点，将下一层所有节点输出到结果中
                    ans.append([node.val for node in curQ])
        return ans

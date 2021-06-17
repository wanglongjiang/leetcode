'''
二叉树的完全性检验
给定一个二叉树，确定它是否是一个完全二叉树。

百度百科中对完全二叉树的定义如下：

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。
（注：第 h 层可能包含 1~ 2h 个节点。）

 

示例 1：



输入：[1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
示例 2：



输入：[1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。
 

提示：

树中将会有 1 到 100 个结点。
'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：BFS
广度优先遍历树，从左到右依次遍历每一层节点，
如果某一层的某个节点缺少了子节点，那么同层的后续节点不允许再有子节点，同层节点必须满2^level个，且下一层节点不能有子节点。
满足上述条件的树，才是完全二叉树。

时间复杂度：O(n)，需要遍历所有节点
空间复杂度：O(n)，设总节点数为n，完全二叉树的最下面一层节点数有可能为n/2+1，需要进入队列
'''


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q, nextq = deque(), deque()
        q.append(root)
        done, level = False, 0
        while q:
            node = q.popleft()
            if node.left:
                if done:
                    return False
                nextq.append(node.left)
            else:
                done = True
            if node.right:
                if done:
                    return False
                nextq.append(node.right)
            else:
                done = True
            if not q and nextq:
                q, nextq = nextq, q
                level += 1
                if not done and len(q) != (1 << level):
                    return False
        return True

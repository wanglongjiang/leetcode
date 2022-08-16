'''
1490. 克隆 N 叉树
给定一棵 N 叉树的根节点 root ，返回该树的深拷贝（克隆）。

N 叉树的每个节点都包含一个值（ int ）和子节点的列表（ List[Node] ）。

class Node {
    public int val;
    public List<Node> children;
}
N 叉树的输入序列用层序遍历表示，每组子节点用 null 分隔（见示例）。

进阶：你的答案可以适用于克隆图问题吗？

 

示例 1：



输入：root = [1,null,3,2,4,null,5,6]
输出：[1,null,3,2,4,null,5,6]
示例 2：



输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 

提示：

给定的 N 叉树的深度小于或等于 1000。
节点的总个数在 [0, 10^4] 之间
'''
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


'''
思路：TODO
'''


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        pass

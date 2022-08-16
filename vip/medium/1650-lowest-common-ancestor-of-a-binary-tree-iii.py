'''
1650. 二叉树的最近公共祖先 III
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。

每个节点都包含其父节点的引用（指针）。Node 的定义如下：

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q 的最深节点（我们允许一个节点为自身的一个后代节点）”。一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。



示例 1:


输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和 1 的最近公共祖先是 3。
示例 2:


输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和 4 的最近公共祖先是 5，根据定义，一个节点可以是自身的最近公共祖先。
示例 3:

输入: root = [1,2], p = 1, q = 2
输出: 1


提示:

树中节点个数的范围是 [2, 10^5]。
-10^9 <= Node.val <= 10^9
所有的 Node.val 都是互不相同的。
p != q
p 和 q 存在于树中。
'''
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


'''
思路：哈希
首先遍历p及其祖先，将其加入哈希表。
然后遍历q及其祖先，如果遍历过程中某个节点与哈希表中重合，该节点就是LCA

时间复杂度：O(h)
空间复杂度：O(h)
'''


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hashmap = {}
        while p:
            hashmap[p.val] = p
            p = p.parent
        while q:
            if q.val in hashmap:
                return hashmap[q.val]
            q = q.parent

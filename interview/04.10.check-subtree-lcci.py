'''
面试题 04.10. 检查子树
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

注意：此题相对书上原题略有改动。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：递归
1. 递归在t1中查找t2，如果能找到，进入2
2. 递归对比2个子树的每个节点是否相同

该题与 剑指 Offer 26.[树的子结构](offer/26-shu-de-zi-jie-gou-lcof.py)类似

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 or not t2:
            return False

        def lookup(node):
            if node.val == t2.val:
                return comp(node, t2)
            if node.left:
                if lookup(node.left):
                    return True
            if node.right:
                if lookup(node.right):
                    return True
            return False

        def comp(node1, node2):
            if node1.val != node2.val:
                return False
            if node1.left and node2.right:
                if not comp(node1.left, node2.left):
                    return False
            elif node1.left or node2.left:
                return False
            if node1.right and node2.right:
                if not comp(node1.right, node2.right):
                    return False
            elif node1.right or node2.right:
                return False
            return True

        return lookup(t1)

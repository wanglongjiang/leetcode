'''
完全二叉树插入器

完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
CBTInserter.get_root() 将返回树的头节点。
 

示例 1：

输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
输出：[null,1,[1,2]]
示例 2：

输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
输出：[null,3,4,[1,2,3,4,5,6,7,8]]
 

提示：

最初给定的树是完全二叉树，且包含 1 到 1000 个节点。
每个测试用例最多调用 CBTInserter.insert  操作 10000 次。
给定节点或插入节点的每个值都在 0 到 5000 之间。
'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：BFS
1. 初始化函数找到倒数第2层（如果最后一层不满），和倒数第1层，分别加入2个队列：q,nextq
2. insert函数将新节点作为q第1个节点的左子树或右子树，如果q的2个节点都已满，将其从队列中移出
3. getroot函数返回root

时间复杂度：初始化函数为O(n)，insert为O(1),get_root为O(1)
空间复杂度：O(n)
'''


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.q, self.nq = deque(), deque()
        self.root = root
        self.q.append(root)
        while self.q:
            node = self.q[0]
            if node.left:
                self.nq.append(node.left)
            else:
                break
            if node.right:
                self.nq.append(node.right)
                self.q.popleft()
            else:
                break
            if not self.q:
                self.q, self.nq = self.nq, self.q

    def insert(self, v: int) -> int:
        newnode = TreeNode(v)
        node = self.q[0]
        if not node.left:
            node.left = newnode
        else:
            node.right = newnode
            self.q.popleft()
        if not self.q:
            self.q, self.nq = self.nq, self.q
        return node.val

    def get_root(self) -> TreeNode:
        return self.root

'''
剑指 Offer II 043. 往完全二叉树添加节点
完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧。

设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

CBTInserter(TreeNode root) 使用根节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
CBTInserter.get_root() 将返回树的根节点。
 

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
 

注意：本题与主站 919 题相同： https://leetcode-cn.com/problems/complete-binary-tree-inserter/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/NaqhDT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
思路：队列 BFS
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
        self.nq.append(newnode)
        if not self.q:
            self.q, self.nq = self.nq, self.q
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


null = None
s = CBTInserter(fromList([1]))
print(s.insert(2))
print(s.insert(3))
print(s.insert(4))
print(s.get_root().val)

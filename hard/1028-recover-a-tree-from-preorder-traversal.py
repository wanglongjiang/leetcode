'''
从先序遍历还原二叉树

我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

 

示例 1：



输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
示例 2：



输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]
示例 3：



输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]
 

提示：

原始树中的节点数介于 1 和 1000 之间。
每个节点的值介于 1 和 10 ^ 9 之间。
'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
思路：DFS
1. 将收入字符串traversal，转化为队列，每个元素为(depth,val)的元组
2. 从队列中取一个元素，
> 2.1 如果深度与当前期望深度一致，创建一个节点，设置为父节点的左子节点
>> 2.1.1 如果下一个与当前深度一致，设置为右节点
>> 2.1.2 如果下一个大于当前深度，需要设置将左子树设置为父节点，递归处理;递归处理完毕后，再尝试将队列中第1个作为右节点
>> 2.1.3 经过2.1.1和2.1.2，有了右节点之后，尝试将后面的节点设置为右节点的子节点处理
> 2.2 返回上一层，上层父节点或祖父节点会尝试作为右节点处理

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        # 转化收入为(depth, val)元组
        q = deque()
        i, n = 0, len(traversal)
        while i < n:
            depth = 0
            while traversal[i] == '-':
                i += 1
                depth += 1
            start = i
            while i < n and traversal[i] != '-':
                i += 1
            q.append((depth, int(traversal[start:i])))

        # 深度遍历生成树
        def dfs(parent, needDepth):
            if q and q[0][0] == needDepth:  # 尝试设置为左节点
                item = q.popleft()
                leftNode = TreeNode(val=item[1])
                parent.left = leftNode
            if q:
                if q[0][0] == needDepth:  # 设置为右节点
                    item = q.popleft()
                    parent.right = TreeNode(val=item[1])
                else:
                    if q[0][0] > needDepth:  # 左子树的下级节点
                        dfs(leftNode, needDepth + 1)
                    if q and q[0][0] == needDepth:  # 右子树
                        item = q.popleft()
                        parent.right = TreeNode(val=item[1])
            if q and q[0][0] > needDepth and parent.right:  # 右子树下级节点
                dfs(parent.right, needDepth + 1)

        dummyRoot = TreeNode()
        dfs(dummyRoot, 0)
        return dummyRoot.left


def toList(node: TreeNode):
    li = []
    if node is None:
        return li
    queue = [node]
    li.append(node.val)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        if node.left:
            queue.append(node.left)
            li.append(node.left.val)
        else:
            li.append(None)
        if node.right:
            queue.append(node.right)
            li.append(node.right.val)
        else:
            li.append(None)

    # 删掉末尾的null
    i = len(li) - 1
    while i > 0:
        if li[i] is None:
            del li[i]
        else:
            break
        i -= 1
    return li


s = Solution()
print(toList(s.recoverFromPreorder("1-2--3--4-5--6--7")))
print(toList(s.recoverFromPreorder("1-2--3---4-5--6---7")))
print(toList(s.recoverFromPreorder("1-401--349---90--88")))

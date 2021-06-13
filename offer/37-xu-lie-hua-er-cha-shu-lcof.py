'''
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \\
  2   3
     / \\
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路，队列
leetcode是层序遍历，按照层序遍历的顺序遍历。
序列化很简单，每层输出后将左右子节点放入队列中，输出直至队列为空。
反序列化需要维护父节点指针，子节点指针每前进2步，父节点指针前进一步，如果父节点为空，需要跳过空的父节点。

时间复杂度：O(n)
空间复杂度：O(n)，最下面一层字节点全部进入队列，最坏情况下是O(n)
'''


class Codec:
    def serialize(self, root):
        ans = []
        queue = [root]

        while queue:  # 层序遍历树
            node = queue[0]
            del queue[0]
            if node:
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append(None)
        while ans and ans[-1] is None:  # 删除末尾的空节点
            ans.pop()
        return ans

    def deserialize(self, data):
        queue = []
        j = -1
        for i in range(len(data)):
            val = data[i]
            if i & 1:  # 子节点指针前进2步，父节点指针前进一步
                j += 1
            while queue and not queue[j]:  # 需要跳过为空的父节点
                j += 1
            if val is not None:
                node = TreeNode(val)
                if queue:
                    if i & 1:
                        queue[j].left = node
                    else:
                        queue[j].right = node
                queue.append(node)
            else:
                queue.append(None)
        return queue[0] if queue else None

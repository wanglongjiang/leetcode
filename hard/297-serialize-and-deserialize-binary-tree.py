'''
二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
'''
'''
思路，1次迭代。leetcode是层序遍历，按照层序遍历的顺序遍历。
序列化很简单，每层输出后将左右子节点放入队列中，输出直至队列为空。
反序列化需要维护父节点指针，子节点指针每前进2步，父节点指针前进一步，如果父节点为空，需要跳过空的父节点。
时间复杂度：O(n)
空间复杂度：O(n)，最下面一层字节点全部进入队列，最坏情况下是O(n)
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


codec = Codec()
print(codec.serialize(codec.deserialize([1, 2, 3, None, None, 4, 5])))
print(codec.serialize(codec.deserialize([1, 2, 3, None, None, 4, 5, 6, 7])))
print(codec.serialize(codec.deserialize([])))
print(codec.serialize(codec.deserialize([1])))
print(codec.serialize(codec.deserialize([1, 2])))

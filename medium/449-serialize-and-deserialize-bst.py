'''
序列化和反序列化二叉搜索树

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，
以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。

 

示例 1：

输入：root = [2,1,3]
输出：[2,1,3]
示例 2：

输入：root = []
输出：[]
 

提示：

树中节点数范围是 [0, 104]
0 <= Node.val <= 10^4
题目数据 保证 输入的树是一棵二叉搜索树。
 

注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路：采用与leetcode相同的层序遍历
序列化将树通过层序遍历转化为list，然后再转为str
反序列化将str转为list对象，然后再转为树

与297.[二叉树的序列化与反序列化](hard/297-serialize-and-deserialize-binary-tree.py)几乎一样，不同点在于输出输入都是字符串

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
        return repr(ans)

    def deserialize(self, data):
        data = eval(data)
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

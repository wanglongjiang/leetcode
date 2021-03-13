'''
验证二叉树的前序序列化
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \\
   3     2
  / \\  / \\
 4   1  #  6
/ \\/ \\  / \\
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

'''
'''
思路：回溯遍历树。
遍历字符串，按照前序遍历的过程：
    遇到数字，认为其为非空节点。
        期望左子树：
            如果存在后续数字，当前节点作为左子树的根节点入栈，递归进入左子树。
            如果后续为#，左子树为空
            如果没有后续，非法字符串。
        期望右子树：
            如果存在后续数字，递归进入右子树。
            如果后续为#，右子树为空
            如果没有后续，非法字符串
    时间复杂度：O(n)
    空间复杂度：O(n) 最坏情况下为O(n)，平均情况下为O(logn)
'''


class Reader():
    def __init__(self, preorder: str):
        self.nodes = preorder.split(',')
        self.i = 0
        self.n = len(self.nodes)

    def next(self):
        if self.i < self.n:
            self.i += 1
            return self.nodes[self.i - 1]
        return False


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        reader = Reader(preorder)

        def backtrack(node: str):
            if node == '#':
                return True
            left = reader.next()
            if not left:
                return False
            if left != '#':
                if not backtrack(left):
                    return False
            right = reader.next()
            if not right:
                return False
            if right != '#':
                if not backtrack(right):
                    return False
            return True

        root = reader.next()
        if root:
            return backtrack(root) and not reader.next()
        return True


s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(s.isValidSerialization("1,#"))
print(s.isValidSerialization("9,#,#,1"))
print(s.isValidSerialization('#'))
print(s.isValidSerialization('#,#'))

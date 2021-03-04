'''
扰乱字符串
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
'''
'''
思路：
思路1，暴力遍历树的所有可能交换，对于长度为n的字符串，有2^n个
思路2，对于每层树，检查集合是否相同。2n*log(n)
'''


class Node:
    def __init__(self, s: str):
        super().__init__()
        self.size = len(s)
        self.charMap = {}
        self.left = None
        self.right = None
        self.otherLeft = None
        self.otherRight = None
        for ch in s:
            if ch in self.charMap:
                self.charMap[ch] += 1
            else:
                self.charMap[ch] = 1

    def isMatch(self, s):
        if len(s) != self.size:
            return False
        for ch in s:
            if ch in self.charMap and self.charMap[ch] > 0:
                self.charMap[ch] -= 1
            else:
                return False
        return True


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 构造集合树
        def makeMapTree(s: str):
            tree = Node(s)
            if tree.size > 2:
                leftSize = tree.size // 2
                tree.left = Node(s[0:leftSize])
                tree.right = Node(s[leftSize:])
            return tree

        tree = makeMapTree(s1)

        # 回溯判断是否匹配
        def backtrack(tree: Node, s: str):
            if not tree.isMatch(s):
                return False
            if len(s) > 2:
                leftSize = tree.size // 2
                rightSize = tree.size - leftSize
                if tree.left and tree.left.isMatch(s[0:leftSize]) and tree.right and tree.right.isMatch(s[leftSize:]):
                    return True
                elif tree.right and tree.right.isMatch(s[0:leftSize]) and tree.left and tree.left.isMatch(s[leftSize:]):
                    return True
                if leftSize != rightSize:
                    if tree.left and tree.left.isMatch(s[0:rightSize]) and tree.right and tree.right.isMatch(s[rightSize:]):
                        return True
                    elif tree.right and tree.right.isMatch(s[0:rightSize]) and tree.left and tree.left.isMatch(s[rightSize:]):
                        return True
                return False

        return backtrack(tree, s2)


s = Solution()
print(s.isScramble(s1="great", s2="rgeat"))
print(s.isScramble(s1="abcde", s2="caebd"))

'''
剑指 Offer 19. 正则表达式匹配

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
'''
'''
思路：使用NFA。
使用有向无权图模拟NFA，然后用深度优先算法解决问题。
相比动态规划的好处是后面可以逐步扩展，将正则表达式的各种特性加入。同时时间复杂度上好。
1、NFA读入p，并编译成有向无权图
2、读入s，用深度优先搜索的方法尝试匹配

时间复杂度：O(m+n) 编译模式为O(m)，匹配过程为O(n)
空间复杂度：O(m) 模式匹配编译后的图会占用空间
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nfa = NFA(p)
        return nfa.matches(s)


class NFA:
    def __init__(self, regex: str):
        super().__init__()
        self.re = regex
        self.statusNum = len(regex)
        self.graph = Digraph(self.statusNum + 1)
        self.compile()

    def compile(self):
        for i in range(self.statusNum):
            if i < self.statusNum - 1 and self.re[i + 1] == '*':
                self.graph.addEdge(i, i + 1)
                self.graph.addEdge(i + 1, i)
            if self.re[i] == '*':
                self.graph.addEdge(i, i + 1)

    def matches(self, txt: str):
        pc = set()
        dfs = DirectedDFS(self.graph, [0])
        for v in range(self.graph.V):
            if dfs.marked[v]:
                pc.add(v)
        for i in range(len(txt)):
            match = set()
            for v in pc:
                if v < self.statusNum:
                    if self.re[v] == txt[i] or self.re[v] == '.':
                        match.add(v + 1)
            pc = set()
            dfs = DirectedDFS(self.graph, match)
            for v in range(self.graph.V):
                if dfs.marked[v]:
                    pc.add(v)
        return self.statusNum in pc


class Digraph:
    def __init__(self, V=0):
        super().__init__()
        self.V = V
        self.E = 0
        self.adj = [[] for i in range(V)]

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.E += 1


class DirectedDFS:
    def __init__(self, G: Digraph, sources):
        super().__init__()
        self.marked = [False] * G.V
        for s in sources:
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G: Digraph, v: int):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

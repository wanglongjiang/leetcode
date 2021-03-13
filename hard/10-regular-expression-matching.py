'''
正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
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


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "aa"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aa", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))

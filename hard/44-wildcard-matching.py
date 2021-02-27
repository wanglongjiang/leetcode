'''
通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

'''
'''
思路：问题与第10题正则表达式几乎一样，使用NFA
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
                    if self.re[v] == txt[i] or self.re[v] == '?':
                        match.add(v + 1)
                    elif self.re[v] == '*':
                        match.add(v)
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
print(s.isMatch("aa", "*"))
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "aa"))
print(s.isMatch("cb", "?b"))
print(s.isMatch("cb", "?a"))
print(s.isMatch("adceb", "*a*b"))
print(s.isMatch("acdcb", "a*c?b"))

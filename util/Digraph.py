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

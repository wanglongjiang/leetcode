'''
克隆图
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}

提示：

节点数不超过 100 。
每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
图是连通图，你可以从给定节点访问到所有节点。
'''


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = []


'''
思路，图的遍历。
提示中告诉我们是简单图，通过1个顶点可以到达所有顶点。可以从1个顶点出发，复制所有节点。
时间复杂度：O(n)，所有节点被遍历1次
空间复杂度：O(n)，需要额外的哈希表存储所有顶点
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodes = {}
        # 深度遍历所有节点
        marked = set()

        def dfs(node: Node):
            marked.add(node.val)
            newnode = ensure(node)
            for nextNode in node.neighbors:
                nextNew = ensure(nextNode)
                newnode.neighbors.append(nextNew)  # 为新旧顶点建立边
                if nextNode.val not in marked:
                    dfs(nextNode)

        def ensure(node):
            if node.val not in nodes:
                newNode = Node(node.val)
                newNode.neighbors = []
                nodes[node.val] = newNode
            return nodes[node.val]

        dfs(node)
        return nodes[node.val]

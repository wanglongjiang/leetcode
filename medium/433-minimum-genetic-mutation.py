'''
最小基因变化

一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，
请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意：

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
 

示例 1：

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

返回值: 1
示例 2：

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

返回值: 2
示例 3：

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

返回值: 3
'''
from typing import List
from collections import defaultdict
from collections import deque
'''
思路：图的最短路径(BFS)+信息压缩
任意2个基因之间如果只有1位差异，则说明2个基因之间有条路径。
可以将所有基因（基因库+开始基因）加入图中，每个基因是一个节点，然后搜索从开始基因到结果基因的路径，找到最短的那条路径，返回其长度。

具体算法：
1. 将基因库、开始基因都转成一个整数编码（每个字符用2bit表示，一个基因可以用16位整数表示）
2. 建立基因的邻接表表示的图
3. 用BFS从开始基因搜索到达结果基因的最短路径

时间复杂度：O(m+n)，m为基因库大小，n为边的数量
空间复杂度：O(m+n)
'''


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        mp = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        # 1. 基因转成整数
        g = {}
        for gene in bank:
            code = 0
            for i in range(8):
                code |= mp[gene[i]] << (7 - i) * 2
            g[code] = set()
        startCode = 0
        for i in range(8):  # 开始基因编码
            startCode |= mp[start[i]] << (7 - i) * 2
        g[startCode] = set()
        endCode = 0
        for i in range(8):  # 开始基因编码
            endCode |= mp[end[i]] << (7 - i) * 2
        # 2. 将只有1位不同的基因之间添加边
        for i in range(8):
            mask = ~(3 << 2 * i)
            group = defaultdict(list)  # 只有1位不同的，都添加到同一分组中
            for gene in g.keys():
                group[gene & mask].append(gene)
            for genes in group.values():
                if len(genes) > 1:
                    for gene in genes:
                        g[gene].update(genes)  # 添加同一分组中的路径
                        g[gene].remove(gene)  # 删除自身到自身的路径

        # 用BFS搜索最短路径
        q, nextq = deque(), deque()
        q.append(startCode)
        ans = 0
        visited = dict.fromkeys(g.keys(), False)
        while q:
            gene = q.popleft()
            visited[gene] = True
            for nextGene in g[gene]:
                if nextGene == endCode:
                    return ans + 1
                if not visited[nextGene]:
                    nextq.append(nextGene)
            if len(q) == 0:
                q, nextq = nextq, q
                ans += 1

        return -1


s = Solution()
print(s.minMutation("AACCGGTT", "AACCGCTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(s.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))

'''
统计好节点的数目
'''
from typing import List

'''
思路：DFS
1、构造邻接表树
2、从根节点开始DFS，如果是叶子节点是好节点，如果不是叶子节点，每个子节点包含的节点数相同，则是好节点
'''
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # 构造邻接表树
        tree = {}
        for u, v in edges:
            if u not in tree:
                tree[u] = []
            if v not in tree:
                tree[v] = []
            tree[u].append(v)
            tree[v].append(u)
        # 好节点数
        good_nodes = 0
        # dfs
        def dfs(node, parent=None):
            nonlocal good_nodes
            if node not in tree:
                good_nodes += 1
                return 1
            is_good = 1 # 是否是好节点
            all_child_count = 1 # 包含自己
            child_count = 0 # 子节点包含的节点数
            for child in tree[node]:
                if child == parent: # 避免重复遍历
                    continue
                count = dfs(child, node)
                all_child_count += count # 所有子节点包含的节点数
                if child_count != 0 and count != child_count: # 如果子节点包含的节点数不同，则不是好节点
                    is_good = 0
                child_count = count # 记录子节点包含的节点数
            good_nodes += is_good # 如果是好节点，加1
            return all_child_count
        dfs(0)
        return good_nodes

s = Solution()
assert s.countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]])==6
assert s.countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])==7
assert s.countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]])==6
assert s.countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]])==12
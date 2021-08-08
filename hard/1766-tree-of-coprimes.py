'''
互质树
给你一个 n 个节点的树（也就是一个无环连通无向图），节点编号从 0 到 n - 1 ，且恰好有 n - 1 条边，每个节点有一个值。树的 根节点 为 0 号点。

给你一个整数数组 nums 和一个二维数组 edges 来表示这棵树。nums[i] 表示第 i 个点的值，
edges[j] = [uj, vj] 表示节点 uj 和节点 vj 在树中有一条边。

当 gcd(x, y) == 1 ，我们称两个数 x 和 y 是 互质的 ，其中 gcd(x, y) 是 x 和 y 的 最大公约数 。

从节点 i 到 根 最短路径上的点都是节点 i 的祖先节点。一个节点 不是 它自己的祖先节点。

请你返回一个大小为 n 的数组 ans ，其中 ans[i]是离节点 i 最近的祖先节点且满足 nums[i] 和 nums[ans[i]] 是 互质的 ，
如果不存在这样的祖先节点，ans[i] 为 -1 。

 

示例 1：



输入：nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
输出：[-1,0,0,1]
解释：上图中，每个节点的值在括号中表示。
- 节点 0 没有互质祖先。
- 节点 1 只有一个祖先节点 0 。它们的值是互质的（gcd(2,3) == 1）。
- 节点 2 有两个祖先节点，分别是节点 1 和节点 0 。节点 1 的值与它的值不是互质的（gcd(3,3) == 3）但节点 0 的值是互质的(gcd(2,3) == 1)，
所以节点 0 是最近的符合要求的祖先节点。
- 节点 3 有两个祖先节点，分别是节点 1 和节点 0 。它与节点 1 互质（gcd(3,2) == 1），所以节点 1 是离它最近的符合要求的祖先节点。
示例 2：



输入：nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
输出：[-1,0,-1,0,0,0,-1]
 

提示：

nums.length == n
1 <= nums[i] <= 50
1 <= n <= 10^5
edges.length == n - 1
edges[j].length == 2
0 <= uj, vj < n
uj != vj

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/tree-of-coprimes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：DFS 哈希
从题目中知道：1 <= nums[i] <= 50，可以先求出1..50每个数字的互质数，并保存到数组primes中。primes[i]是数字i的所有互质数。
然后用DFS遍历树，设一个哈希表hashmap，value为当前节点的索引，key为节点对应的互质数
> 1. 每遍历到一个节点node，就查找hashmap中是否有key=node.value，如果有，hashmap[key]即为其祖先
> 2. 然后从primes中取到当前节点的互质数，将其作为key，当前节点的索引i作为value加入hashmap。（这个过程可能会覆盖hashmap中的互质数的索引，确保处理子节点时索引是最近祖先）
> 3. 如果有子节点，递归处理子节点。注意：每处理一个子节点，需要按照2，重新设置hashmap，恢复可能被左子树删除的互质数索引。
> 4. 当前节点及子节点全部处理完了之后，需要删除当前节点在hashmap中添加的互质数索引。

时间复杂度：O(h)，h为树的高度，最坏情况下是O(n)，hashmap中最多可能有50个数字，虽然每个节点都需要维护hashmap，但也可以视为常数。
空间复杂度：O(h)
'''


class Solution:
    def __init__(self):
        self.primes = [set() for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if self.gcd(i, j) == 1:
                    self.primes[i].add(j)
                    self.primes[j].add(i)

    def gcd(self, a, b):
        while a % b:
            a, b = b, a % b
        return b

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        # 生成邻接表形式的图
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        # DFS遍历所有节点
        marked = [False] * n
        marked[0] = True
        hashmap = {}
        ans = [-1] * n

        def dfs(node):
            if nums[node] in hashmap:
                ans[node] = hashmap[nums[node]]
            changed = False  # 标记当前节点是否修改过hashmap
            for nextnode in g[node]:
                if not marked[nextnode]:
                    marked[nextnode] = True
                    changed = True
                    # 将node的所有互质数加入hashmap
                    for p in self.primes[nums[node]]:
                        hashmap[p] = node
                    # 递归处理子节点
                    dfs(nextnode)
            if changed:  # 删除当前节点加入的互质数
                for p in self.primes[nums[node]]:
                    if p in hashmap:
                        del hashmap[p]

        dfs(0)
        return ans


s = Solution()
print(s.getCoprimes(nums=[2, 3, 3, 2], edges=[[0, 1], [1, 2], [1, 3]]))
print(s.getCoprimes(nums=[5, 6, 10, 2, 3, 6, 15], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))

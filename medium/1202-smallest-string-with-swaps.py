'''
交换字符串中的元素

给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，
其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

 

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"
 

提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母
'''
from typing import List
'''
思路：并查集
1. 用并查集将有连结的位置连结到一起
2. 遍历字符串，将同一个集合的字符统计到一个大小为26的计数数组中
3. 遍历字符串的每一个位置，按照并查集结果和字典顺序，将计数数组的字符输出到结果字符串中

时间复杂度：O(n)
空间复杂度：O(n)
'''


# 定义并查集
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        # 1.用并查集连结可以交换的位置
        union = UnionFind(n)
        for pair in pairs:
            union.unite(pair[0], pair[1])
        # 2. 遍历字符串，将同一个集合的字符统计到一个大小为26的计数数组中
        counter = {}
        for i in range(n):
            root = union.find(i)
            if root not in counter:
                counter[root] = [0] * 26
            counter[root][ord(s[i]) - ord('a')] += 1
        # 将计数数组转储成字符list
        c = {}
        for i, arr in counter.items():
            li = []
            for j in range(25, -1, -1):
                for k in range(arr[j]):
                    li.append(chr(ord('a') + j))
            c[i] = li
        # 3.遍历字符串的每一个位置，按照并查集结果和字典顺序，将计数数组的字符输出到结果字符串中
        ans = []
        for i in range(n):
            root = union.find(i)
            ans.append(c[root].pop())
        return ''.join(ans)


s = Solution()
print(s.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
print(s.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
print(s.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))

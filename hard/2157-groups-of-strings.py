'''
2157. 字符串分组
给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。

如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ：

往 s1 的字母集合中添加一个字母。
从 s1 的字母集合中删去一个字母。
将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。

注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。

请你返回一个长度为 2 的数组 ans ：

ans[0] 是 words 分组后的 总组数 。
ans[1] 是字符串数目最多的组所包含的字符串数目。
 

示例 1：

输入：words = ["a","b","ab","cde"]
输出：[2,3]
解释：
- words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 words[1] 和 words[2] 关联。
- words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 words[0] 和 words[2] 关联。
- words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 words[1] 关联。
- words[3] 与 words 中其他字符串都不关联。
所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。
示例 2：

输入：words = ["a","ab","abc"]
输出：[1,3]
解释：
- words[0] 与 words[1] 关联。
- words[1] 与 words[0] 和 words[2] 关联。
- words[2] 与 words[1] 关联。
由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
所以最大的组大小为 3 。
 

提示：

1 <= words.length <= 2 * 104
1 <= words[i].length <= 26
words[i] 只包含小写英文字母。
words[i] 中每个字母最多只出现一次。
'''
from collections import defaultdict
from typing import List
'''
思路：状态压缩+并查集
看到题目是求分组个数和分组大小，第一反应就是用并查集。
每个字符串还可以映射成一个26bit数字。
计算任意2个字符串是否能联通时，如果采用暴力比较，那么时间复杂度为O(10^8)，大概率超时
如果采用对字符串进行“变形”，变成能联通字符串的字符，这种方式，一个字符串的变形数大概不到200：1变成0，0变成1共26个，然后1个1变成0，0变成1，大概不到200
时间复杂度降到了O(10^6)

时间复杂度：O(100n)
空间复杂度：O(n)
'''


# 哈希版本的并查集
class UnionFind:
    def __init__(self, count) -> None:
        self.count = count  # 记录每个字符串的并查集的大小
        self.parent = {mask: mask for mask in count.keys()}  # 记录并查集的所属集合
        self.maxSize = max(count.values())  # 最大的组的大小
        self.groupNum = len(count)  # 组的个数

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if y not in self.count:  # 只有联通的字符串在并查集中存在才允许添加
            return
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if rootx > rooty:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            self.groupNum -= 1  # 2个组进行了合并，组的数量-1
            self.count[rootx] += self.count[rooty]  # 组的大小扩张了
            self.maxSize = max(self.maxSize, self.count[rootx])  # 更新最大的组的大小


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # 将字符串映射为数字，并统计个数
        count = defaultdict(int)
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            count[mask] += 1
        # 添加到并查集
        uf = UnionFind(count)
        # 遍历所有数字，再将其所有“联通”加入并查集
        for mask in count.keys():
            for i in range(26):
                uf.union(mask, mask ^ (1 << i))  # 1变成0，0变成1。也即为：从 s1 的字母集合中删去一个字母。往 s1 的字母集合中添加一个字母。
                if mask & (1 << i):
                    for j in range(26):
                        if not mask & (1 << j):
                            uf.union(mask, (mask | (1 << j)) ^ (1 << i))  # 1位1变成0同时1位0变成1，即：将 s1 中的一个字母替换成另外任意一个字母
        return [uf.groupNum, uf.maxSize]


s = Solution()
print(s.groupStrings(["a", "b"]))
print(s.groupStrings(["b", "q"]))

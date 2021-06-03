'''
情侣牵手
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

示例 1:

输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。
示例 2:

输入: row = [3, 2, 0, 1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。
说明:

len(row) 是偶数且数值在 [4, 60]范围内。
可以保证row 是序列 0...len(row)-1 的一个全排列。
'''
from typing import List
'''
思路：并查集
将座位视为n个情侣座，每2个座位是1个情侣座，可以发现如果初始坐在同一情侣座的所有人都不是情侣。
每个情侣座可以将坐在偶数座位号上的人固定，坐在奇数座位号的人与其他人交换位置，
因为每次交换可以成功牵手1个情侣，最后1次交换可以牵手2个情侣，最多n-1次就可以全部交换完成。
上面是交换最多的情况下，但实际上例如有4个情侣座，他们如果正好是22交换的情况下，只需要2次交换，不需要3次。
这种情况下是因为情侣的交换划分成了2个区，每个区内只需要与区内的进行交换即可。

根据上面的思路写出算法：
1. 遍历row，将情侣编号row[i]/2和座位索引i/2作为key,val加入哈希表
2. 建立大小为n的并查集
3. 再次遍历row,对于当前情侣和座位编号
> 如果与其相同情侣编号的座位号也相同，跳过
> 如果不相同，需要交换，将2个座位号加入并查集
4. 在并查集中查询所有座位号的同区根座位号，并对根座位号进行计数
5. 对于同区座位>1的累计交换次数，每个区的交换次数为座位数-1

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
    def minSwapsCouples(self, row: List[int]) -> int:
        seatMap = {}
        n = len(row)
        for i in range(n):  # 1.遍历row，将情侣编号row[i]/2和座位索引i/2作为key,val加入哈希表
            seatMap[row[i] // 2] = i // 2
        union = UnionFind(n // 2)  # 2.建立并查集
        for i in range(n):  # 3. 再次遍历row
            if seatMap[row[i] // 2] != i // 2:  # 情侣的座位号不同的2个座位号加入并查集
                union.unite(seatMap[row[i] // 2], i // 2)
        count = [0] * (n // 2)
        for i in range(n // 2):  # 4.在并查集中查询所有座位号的同区根座位号，并对根座位号进行计数
            count[union.find(i)] += 1
        ans = 0
        for c in count:  # 5.对于同区座位>1的累计交换次数，每个区的交换次数为座位数-1
            if c > 1:
                ans += c - 1
        return ans


s = Solution()
print(s.minSwapsCouples([0, 2, 1, 3]))
print(s.minSwapsCouples([3, 2, 0, 1]))

'''
1386. 安排电影院座位


如上图所示，电影院的观影厅中有 n 行座位，行编号从 1 到 n ，且每一行内总共有 10 个座位，列编号从 1 到 10 。

给你数组 reservedSeats ，包含所有已经被预约了的座位。比如说，researvedSeats[i]=[3,8] ，它表示第 3 行第 8 个座位被预约了。

请你返回 最多能安排多少个 4 人家庭 。4 人家庭要占据 同一行内连续 的 4 个座位。
隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。



示例 1：



输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
输出：4
解释：上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。
示例 2：

输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
输出：2
示例 3：

输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
输出：4


提示：

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
所有 reservedSeats[i] 都是互不相同的。
'''
from typing import List
from collections import defaultdict
'''
思路：哈希 位运算
经分析，1，10列是没有用的，对安排座位有影响的是2~9列。
2~5列如果空白，可以放置一个家庭
6~9列如果空白，可以放置一个家庭
经过上述2个判断，如果没有家庭被放置，再判断4~7是否空白，如果空白，可以放置一个家庭，否则该行作废。

可以遍历reservedSeats，用一个哈希表保存各行的座位占用情况，key为行号，用一个整数的1~10位保存一行的占用情况。
然后初始化总的家庭数ans=2*n（最多安排2*n个家庭）
再遍历哈希表，针对每一行，按照上面的分析计算出家庭数，ans += 计算出的家庭数-2

时间复杂度：O(m)，m=reservedSeats.length
空间复杂度：O(m)
'''


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        for seat in reservedSeats:
            hashmap[seat[0]] |= 1 << seat[1]  # 把一行的座位占用情况保存到整数中
        ans = 2 * n
        mask2to5, mask6to9, mask4to7 = 0xf << 2, 0xf << 6, 0xf << 4  # 2~5列，6~9列，4~7列的掩码
        for seat in hashmap.values():
            num = 0
            if mask2to5 & seat == 0:  # 2~5列如果空白，可以放置一个家庭
                num += 1
            if mask6to9 & seat == 0:  # 6~9列如果空白，可以放置一个家庭
                num += 1
            if num == 0 and mask4to7 & seat == 0:  # 判断4~7是否空白，如果空白，可以放置一个家庭，否则该行作废。
                num = 1
            ans += num - 2
        return ans


s = Solution()
print(s.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(s.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(s.maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))

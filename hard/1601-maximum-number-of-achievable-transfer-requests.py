'''
1601. 最多可达成的换楼请求数目
我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。

给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。

一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。

请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

 

示例 1：



输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。
示例 2：



输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。
示例 3：

输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4
 

提示：

1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n
'''

from typing import List
'''
思路：二进制枚举
我们可以使用一个长度为 mm 的二进制数 \textit{mask}mask 表示所有的请求，其中 \textit{mask}mask 从低到高的第 ii 位为 11 表示选择第 ii 个请求，为 00 表示不选第 ii 个请求。我们可以枚举 [0,2^m-1][0,2 
m
 −1] 范围内的所有 \textit{mask}mask，对于每个 \textit{mask}mask，依次枚举其每一位，判断是否为 11，并使用与方法一相同的数组 \textit{delta}delta 以及变量 \textit{cnt}cnt 进行统计，在满足要求时更新答案。

时间复杂度：O(2^m \times n)O(2 
m
 ×n)，其中 mm 是数组 \textit{requests}requests 的长度，即请求的数量。从 mm 个请求中任意选择请求的方案数为 2^m2 
m
 ，对于每一种方案，我们需要 O(n)O(n) 的时间判断其是否满足要求。

空间复杂度：O(n)O(n)。数组 \textit{delta}delta 需要 O(n)O(n) 的空间。

'''


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans

'''
2280. 表示一个折线图的最少线段数
给你一个二维整数数组 stockPrices ，其中 stockPrices[i] = [dayi, pricei] 表示股票在 dayi 的价格为 pricei 。
折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。比方说下图是一个例子：


请你返回要表示一个折线图所需要的 最少线段数 。

 

示例 1：



输入：stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
输出：3
解释：
上图为输入对应的图，横坐标表示日期，纵坐标表示价格。
以下 3 个线段可以表示折线图：
- 线段 1 （红色）从 (1,7) 到 (4,4) ，经过 (1,7) ，(2,6) ，(3,5) 和 (4,4) 。
- 线段 2 （蓝色）从 (4,4) 到 (5,4) 。
- 线段 3 （绿色）从 (5,4) 到 (8,1) ，经过 (5,4) ，(6,3) ，(7,2) 和 (8,1) 。
可以证明，无法用少于 3 条线段表示这个折线图。
示例 2：



输入：stockPrices = [[3,4],[1,2],[7,8],[2,3]]
输出：1
解释：
如上图所示，折线图可以用一条线段表示。
 

提示：

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
所有 dayi 互不相同 。
'''

from typing import List
'''
思路：排序 几何
排序后，依次计算2个点形成的角的tan值，如果发生变化则有新的线段。
因为除法精度问题，将除法改成乘法，过了。

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda p: p[0])
        ans, prey, prex = 0, 1, 0
        for i in range(1, len(stockPrices)):
            p1, p2 = stockPrices[i - 1], stockPrices[i]
            dy, dx = (p2[1] - p1[1]), (p2[0] - p1[0])
            if dy * prex != dx * prey:
                ans += 1
                prex, prey = dx, dy
        return ans


s = Solution()
print(s.minimumLines([[1, 1], [500000000, 499999999], [1000000000, 999999998]]))

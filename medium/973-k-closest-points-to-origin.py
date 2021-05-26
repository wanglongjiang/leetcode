'''
最接近原点的 K 个点
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''
from typing import List
'''
总体思路：欧几里得距离是sqrt(x^2+y^2)，也即比较x^2+y^2大小，取最小的k个数。
对于取最大/最小k个数，有多种算法：

思路1，堆
建立一个大小为k的堆，遍历所有输入，将数据加入堆。最后输出堆指向的元素

时间复杂度：O(nlogk)
空间复杂度：O(n+logk)

思路2，平衡二叉树
用平衡二叉树进行排序
将所有数据用平衡二叉树进行排序。

时间复杂度：O(nlogn)
空间复杂度：O(n)

思路3，分治
用快排里面分区的思路，将数组分成大小2个区，
> 如果小区=k，直接返回;
> 如果小区<k，将小区输出，然后对大区继续分区;
> 如果小区>k，继续对小区分区。

时间复杂度：O(n)平均情况下是O(n)，最坏情况下是O(n^2)
空间复杂度：O(n)

上面3种算法，堆适用于n非常大（甚至大到需要放到磁盘、网络上进行外排序），k较小的情况；
分治算法适用于输入较为随机，数据规模能放到内存内，它的时间复杂度表现不是很稳定，最好情况下是O(n)，最坏情况下是O(n^2)；
平衡二叉树的表现比较稳定。
'''


class Solution:
    # 思路3，分治
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import random
        n = len(points)
        # 将c=x^2+y^2和索引打包成元组(c,index)构成的数组
        d = [(points[i][0] * points[i][0] + points[i][1] * points[i][1], i) for i in range(n)]
        start, end = 0, n - 1
        ans = []
        while k > 0:
            pIndex = random.randint(start, end)
            d[pIndex], d[start] = d[start], d[pIndex]
            pivot = d[start]  # 使用随机的pivot将数组分成2部分
            i, j = start, end
            while i < j:
                while i < j and d[j][0] >= pivot[0]:
                    j -= 1
                d[i] = d[j]
                while i < j and d[i][0] < pivot[0]:
                    i += 1
                d[j] = d[i]
            d[i] = pivot
            lowSize = i - start
            if lowSize == k:
                ans.extend(d[start:i])
                return [points[i] for c, i in ans]
            elif lowSize < k:  # 不够k个数，将lowSize个数加入结果，然后继续对高区进行分区
                ans.extend(d[start:i])
                k -= lowSize
                start = i
            else:  # 超过k个数，将
                end = i - 1


s = Solution()
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))

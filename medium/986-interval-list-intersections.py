'''
986. 区间列表的交集
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。
每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。



示例 1：


输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
示例 2：

输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
示例 3：

输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]
示例 4：

输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]


提示：

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10^9
endi < starti+1
0 <= startj < endj <= 10^9
endj < startj+1
'''
from typing import List
'''
思路：双指针
用2个指针分别指向first和second，
1. 对比2个区间，如果有交集，计算交集，插入结果list
2. 然后区间的结束区间较小的指针向后移动（抛弃结束区间较小的）
3. 重复上述1.2过程

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        p1, p2 = 0, 0
        m, n = len(firstList), len(secondList)
        while p1 < m and p2 < n:
            r1, r2 = firstList[p1], secondList[p2]
            if r1[0] <= r2[0] <= r1[1]:
                ans.append([r2[0], min(r1[1], r2[1])])
            elif r1[0] <= r2[1] <= r1[1]:
                ans.append([max(r1[0], r2[0]), r2[1]])
            elif r2[0] <= r1[0] <= r2[1]:
                ans.append([r1[0], min(r2[1], r1[1])])
            elif r2[0] <= r1[1] <= r2[1]:
                ans.append([max(r1[0], r2[0]), r1[1]])
            if r1[1] > r2[1]:  # 抛弃结束较早的区间
                p2 += 1
            else:
                p1 += 1
        return ans


s = Solution()
print(s.intervalIntersection([[4, 6], [7, 8], [10, 17]], [[5, 10]]))
print(s.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]], secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
print(s.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]))
print(s.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]))

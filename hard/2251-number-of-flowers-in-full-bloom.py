'''
2251. 花期内花的数目
给你一个下标从 0 开始的二维整数数组 flowers ，其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）。
同时给你一个下标从 0 开始大小为 n 的整数数组 persons ，persons[i] 是第 i 个人来看花的时间。

请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。

 

示例 1：



输入：flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
输出：[1,2,2,2]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
示例 2：



输入：flowers = [[1,10],[3,3]], persons = [3,3,2]
输出：[2,2,1]
解释：上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
 

提示：

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= persons.length <= 5 * 104
1 <= persons[i] <= 109
'''
from collections import defaultdict
from typing import List
'''
思路：线段树
遍历flowers中所有区间，然后更新线段树对应的区间，使其值+1。
为节省空间，区间细化到2的指数倍

时间复杂度：O(nlog(10^9))
空间复杂度：O(log(10^9))
'''


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        tree = defaultdict(int)  # 线段树
        MAX = 10**9

        def update(idx, left, right, start, end):  # left,right是线段树的区间；start,end是要更新的区间
            if left > end or right < start:  # 两个区间无重叠
                return
            if left >= start and right <= end:  # 更新区间完全覆盖线段树区间，进行更新
                tree[idx] += 1
            else:
                tree[idx] += 0  # 这条语句建立一层层的子树，避免中间有空挡
                mid = (left + right) // 2  # 区间进行拆分，然后分别进行更新
                update(idx * 2, left, mid, start, end)
                update(idx * 2 + 1, mid + 1, right, start, end)

        # 将开花时间更新到线段树
        for flower in flowers:
            update(1, 1, MAX, flower[0], flower[1])

        # 查询
        def lookup(idx, left, right, day):
            ans = tree[idx]
            mid = (left + right) // 2
            if idx * 2 in tree and left <= day and mid >= day:  # 日期落在左子树，递归查找左子树
                ans += lookup(idx * 2, left, mid, day)
            elif idx * 2 + 1 in tree and mid + 1 <= day and right >= day:  # 日期落在右子树，递归查找右子树
                ans += lookup(idx * 2 + 1, mid + 1, right, day)
            return ans

        return [lookup(1, 1, MAX, i) for i in persons]


s = Solution()
print(s.fullBloomFlowers(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], persons=[2, 3, 7, 11]))

'''
俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

'''
from typing import List
'''
思路：动态规划
1、对整数对进行排序，先按照w,w相同的再按照h，排序后小的肯定在前面，大的在后面
2、能够发现，这个问题具有最优子结构。状态转移方程为：
select(1)=1
select(i)=select(j)+1 max(count[j])满足：j<i，且j[w,h]<i[w,h]
时间复杂度：排序O(nlogn)，计算套娃数需要一次遍历，总计O(nlogn)
空间复杂度：需要辅助数组存储每个位置上的套娃数，O(n)
'''


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        counter = [1] * n  # 每个位置上的套娃数
        maxNums = [1] * n  # 截止该位置最大的套娃数
        envelopes.sort(key=lambda e: (e[0] - 1 / e[1]))  # 先按照w排序，w相同的按照h排序
        for i in range(1, n):
            maxSub = 0
            for j in range(i - 1, -1, -1):  # 向前搜索子套娃
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                    maxSub = max(maxSub, counter[j])
                if maxSub >= maxNums[j]:  # 如果计算得到的子套娃数，大于该位置的最大套娃数，不需要向前搜索了
                    break
            counter[i] += maxSub
            maxNums[i] = max(maxNums[i - 1], counter[i])
        return maxNums[n - 1]


s = Solution()
print(s.maxEnvelopes([[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]))
print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))

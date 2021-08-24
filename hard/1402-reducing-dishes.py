'''
1402. 做菜顺序
一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。

一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。

请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。



示例 1：

输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。
示例 2：

输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)
示例 3：

输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。
示例 4：

输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35


提示：

n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3
'''
from typing import List
'''
思路：贪心 排序
满意度越高的菜越靠后做，产生的价值越高。
首先对满意度进行排序，满意度高的在前面，满意度低的在后面；
然后依次求前缀和，如果前缀和>0，则改满意度的菜有价值，把前缀和累加到结果中。

时间复杂度：O(n$log^n$)
空间复杂度：O(1)
'''


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        ans, s = 0, 0
        for num in satisfaction:
            s += num
            if s > 0:
                ans += s
        return ans

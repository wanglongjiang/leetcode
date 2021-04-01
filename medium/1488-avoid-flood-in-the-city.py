'''
避免洪水泛滥
你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨的时候，如果第 n 个湖泊是空的，那么它就会装满水，
否则这个湖泊会发生洪水。你的目标是避免任意一个湖泊发生洪水。

给你一个整数数组 rains ，其中：

rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
请返回一个数组 ans ，满足：

ans.length == rains.length
如果 rains[i] > 0 ，那么ans[i] == -1 。
如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。

请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例 4）。

提示：
1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9
'''
from typing import List
'''
思路：哈希表暴力搜索。
用哈希表full记录已经下满雨的湖泊，和第几天下雨（下标）；用列表empty记录不下雨的日期
从左到右遍历rains数组，对于第i个元素，rains[i]
    如果==0，将i加入empty。
    如果>0，将(key:rains[i],val:i)加入full中，如果full中存在与rains[i]相同的值rains[j]，在empty中搜索比j大的值，将其从empty中删除
时间复杂度：O(n*n)，搜索及删除empty中的元素，有O(n*n)的复杂度
空间复杂度：O(n)
'''


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        pass


s = Solution()
print(s.avoidFlood([1, 2, 3, 4]))
print(s.avoidFlood([1, 2, 0, 0, 2, 1]))
print(s.avoidFlood([1, 2, 0, 1, 2]))
print(s.avoidFlood([69, 0, 0, 0, 69]))
print(s.avoidFlood([10, 20, 20]))

'''
2456. 最流行的视频创作者
给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i] ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。

视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。

如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。

 

示例 1：

输入：creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
输出：[["alice","one"],["bob","two"]]
解释：
alice 的流行度是 5 + 5 = 10 。
bob 的流行度是 10 。
chris 的流行度是 4 。
alice 和 bob 是流行度最高的创作者。
bob 播放量最高的视频 id 为 "two" 。
alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是 "one" 。
示例 2：

输入：creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
输出：[["alice","b"]]
解释：
id 为 "b" 和 "c" 的视频都满足播放量最高的条件。
由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。
 

提示：

n == creators.length == ids.length == views.length
1 <= n <= 105
1 <= creators[i].length, ids[i].length <= 5
creators[i] 和 ids[i] 仅由小写英文字母组成
0 <= views[i] <= 105
'''
from collections import defaultdict
from typing import List
'''
思路：哈希表
遍历3个数组，用1个哈希表popCreators累计每个作者的流行度，用1个哈希表popIds记录每个作者播放量最高的视频
遍历一次哈希表popCreators，找到流行度最高的作者，将作者名称和视频输出到结果中

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popCreators, popIds = defaultdict(int), {}
        n = len(ids)
        maxpop = 0
        for i in range(n):
            popCreators[creators[i]] += views[i]
            maxpop = max(maxpop, popCreators[creators[i]])
            if creators[i] not in popIds:
                popIds[creators[i]] = (views[i], ids[i])  # 将作者的一个视频id及播放量放入哈希表
            else:
                if views[i] > popIds[creators[i]][0] or (views[i] == popIds[creators[i]][0] and ids[i] < popIds[creators[i]][1]):
                    popIds[creators[i]] = (views[i], ids[i])  # 将作者的播放量最大的视频或者播放量相同但id较小的视频的id及播放量放入哈希表
        ans = []
        for creator, pop in popCreators.items():
            if pop == maxpop:
                ans.append([creator, popIds[creator][1]])
        return ans

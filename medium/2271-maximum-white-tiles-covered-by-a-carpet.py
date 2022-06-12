'''
2271. 毯子覆盖的最多白色砖块数
给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。

同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子。

请你返回使用这块毯子，最多 可以盖住多少块瓷砖。

 

示例 1：



输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
输出：9
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 9 块瓷砖，所以返回 9 。
注意可能有其他方案也可以覆盖 9 块瓷砖。
可以看出，瓷砖无法覆盖超过 9 块瓷砖。
示例 2：



输入：tiles = [[10,11],[1,1]], carpetLen = 2
输出：2
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 2 块瓷砖，所以我们返回 2 。
 

提示：

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
tiles 互相 不会重叠 。
'''

from bisect import bisect_right
from typing import List
'''
思路：排序 二分查找
1、排序数组tiles
2、遍历tiles每个元素，然后在tiles中二分查找tiles[i][0]+carpetLen，
    如果找到了tiles[j]，那么i..j之间的瓷砖可以被覆盖

时间复杂度：O(nlogn)
空间复杂度：O(n)，设置一个开始坐标数组，用于二分查找；设置一个前缀和数组，便于计算i..j之间的辞职数量
'''


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        startIndexs = [t[0] for t in tiles]  # 将开始坐标提取出来二分查找
        prefixSum = [tile[1] - tile[0] + 1 for tile in tiles]  # 计算前缀和
        for i in range(1, len(tiles)):
            prefixSum[i] = prefixSum[i - 1] + prefixSum[i]
        ans = 0
        for i in range(len(tiles)):
            j = bisect_right(startIndexs, startIndexs[i] + carpetLen)  # 二分查找能覆盖的区间
            covered = prefixSum[j - 1] - (prefixSum[i - 1] if i > 0 else 0)
            if startIndexs[i] + carpetLen - 1 < tiles[j - 1][1]:  # 判断是否超过最后一个区间，如果未超过，需要重新计算覆盖的最后一个区间的大小
                covered = covered - (tiles[j - 1][1] - tiles[j - 1][0] + 1) + startIndexs[i] + carpetLen - tiles[j - 1][0]
            ans = max(ans, covered)
        return ans


s = Solution()
print(s.maximumWhiteTiles(tiles=[[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], carpetLen=10))
print(s.maximumWhiteTiles(tiles=[[10, 11], [1, 1]], carpetLen=2))

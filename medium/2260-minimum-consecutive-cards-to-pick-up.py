'''
2260. 必须拿起的最小连续卡牌数
给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。

返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。

 

示例 1：

输入：cards = [3,4,2,3,4,7]
输出：4
解释：拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。
示例 2：

输入：cards = [1,0,5,3]
输出：-1
解释：无法找出含一对匹配卡牌的一组连续卡牌。
 

提示：

1 <= cards.length <= 105
0 <= cards[i] <= 106
'''
from collections import defaultdict
from typing import List
'''
思路：哈希表
用哈希表记录每个元素最近一次出行的索引，当再次出现时，更新更近的2个索引之差

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans, idxMap = float('inf'), {}
        for i, val in enumerate(cards):
            if val in idxMap:
                ans = min(ans, i - idxMap[val] + 1)
                idxMap[val] = i
            else:
                idxMap[val] = i
        return -1 if ans == float('inf') else ans

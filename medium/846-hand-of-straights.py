'''
一手顺子

爱丽丝有一手（hand）由整数数组给定的牌。 

现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。

如果她可以完成分组就返回 true，否则返回 false。

 

注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

 

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
 

提示：

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
'''
from typing import List
from sortedcontainers import SortedDict
'''
思路：有序集合
使用treemap(python中的treemap是sortedcontainers.sorteddict)对所有元素进行计数
然后从小到大，groupSize一组从treempa中删除，如果能出尽则返回true

时间复杂度：O(nlogn),红黑树的时间复杂度为nlogn
空间复杂度：O(n)
'''


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        treemap = SortedDict()
        for num in hand:
            if num in treemap:
                treemap[num] += 1
            else:
                treemap[num] = 1
        # groupSize一组，输出连续的数字
        while treemap:
            num, cnt = treemap.peekitem(0)
            for num in range(num, num + groupSize):
                if num in treemap:
                    treemap[num] -= 1
                    if treemap[num] == 0:
                        del treemap[num]
                else:
                    return False
        return True


s = Solution()
print(s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(s.isNStraightHand([1, 2, 3, 4, 5], 4))

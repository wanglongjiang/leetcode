'''
2274. 不含特殊楼层的最大连续楼层数
Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 特殊楼层 ，仅用于放松。

给你两个整数 bottom 和 top ，表示 Alice 租用了从 bottom 到 top（含 bottom 和 top 在内）的所有楼层。另给你一个整数数组 special ，其中 special[i] 表示  Alice 指定用于放松的特殊楼层。

返回不含特殊楼层的 最大 连续楼层数。

 

示例 1：

输入：bottom = 2, top = 9, special = [4,6]
输出：3
解释：下面列出的是不含特殊楼层的连续楼层范围：
- (2, 3) ，楼层数为 2 。
- (5, 5) ，楼层数为 1 。
- (7, 9) ，楼层数为 3 。
因此，返回最大连续楼层数 3 。
示例 2：

输入：bottom = 6, top = 8, special = [7,6,8]
输出：0
解释：每层楼都被规划为特殊楼层，所以返回 0 。
 

提示

1 <= special.length <= 105
1 <= bottom <= special[i] <= top <= 109
special 中的所有值 互不相同
'''

from typing import List
'''
思路：排序
对special进行排序，排序后相近的楼层靠在一起，然后最大的2个特殊楼层之间的差即为答案

时间复杂度：O(nlogn)，排序需要的时间为O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans, prev = max(special[0] - bottom, top - special[-1]), special[0]
        for i in range(1, len(special)):
            ans = max(ans, special[i] - prev - 1)
            prev = special[i]
        return ans

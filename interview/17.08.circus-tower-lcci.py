'''
面试题 17.08. 马戏团人塔
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。
已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：

height.length == weight.length <= 10000
'''
from typing import List
import bisect
'''
思路：二分查找 LIS
按照身高升序，相同身高的按照体重降序进行排序后，这个问题变成了求体重数组的最长升序子序列（LIS）的问题。
详细算法见代码和注释

简化题目：- 300.[最长递增子序列](medium/300-longest-increasing-subsequence.py)

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        height, weight = zip(*sorted(zip(height, weight), key=lambda p: (p[0], -p[1])))  # 按照身高升序，相同身高逆序的顺序进行排序
        dp = [0] * len(weight)  # dp中存放可能形成最长子序列的元素
        ans = 0  # 存放最长子序列长度
        for w in weight:
            i = bisect.bisect_left(dp, w, 0, ans)  # 二分查找w在已排序好的dp数组中的索引
            dp[i] = w  # 如果i<ans，说明替换了原先dp中较大的值，较小的值进入数组，便于后来者扩展数组的实际元素个数，增加序列长度
            if i == ans:  # 如果w大于dp中所有元素，扩展了最长子序列的长度
                ans += 1
        return ans

'''
吃苹果的最大数目
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，
这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。

提示：

apples.length == n
days.length == n
1 <= n <= 2 * 10^4
0 <= apples[i], days[i] <= 2 * 10^4
只有在 apples[i] = 0 时，days[i] = 0 才成立

'''
from typing import List
'''
思路：设置一个2n长度的数组，计算出每一天苹果数量。
时间复杂度：最坏情况下，每个苹果保质期都是n，那么就是O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        total = [-1] * 2 * n  # 初始每天都需要1个苹果
        for i in range(n):
            apple = apples[i]
            day = days[i]
            for j in range(day):  # 在苹果的有效期内分发苹果
                if total[i + j] < 0:  # 如果这一天需要苹果，将苹果减掉1个
                    apple -= 1
                    total[i + j] = 0
                if apple == 0:  # 苹果已经吃完，不需要向后添加
                    break
                total[i + j] += apple  # 剩余的苹果累加起来
        return 2 * n - total.count(-1)  # 所有天数减去未吃到苹果的天数即为吃到的苹果数


s = Solution()
print(s.eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
print(s.eatenApples(apples=[3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))

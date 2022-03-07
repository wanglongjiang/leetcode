'''
到家的最少跳跃次数

有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。

跳蚤跳跃的规则如下：

它可以 往前 跳恰好 a 个位置（即往右跳）。
它可以 往后 跳恰好 b 个位置（即往左跳）。
它不能 连续 往后跳 2 次。
它不能跳到任何 forbidden 数组中的位置。
跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。

给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，
请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。

 

示例 1：

输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出：3
解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
示例 2：

输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
输出：-1
示例 3：

输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
输出：2
解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
 

提示：

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
forbidden 中所有位置互不相同。
位置 x 不在 forbidden 中。
'''
from typing import List
import math
'''
思路：BFS
当前位置如果是向前跳到的，下一个位置有2个：一个向前跳a步，另外一个是向后跳b步,下一个位置不能在forbidden里面
当前位置如果是向后跳到的，下一个位置有1个：向前跳a步，下一个位置不能在forbidden里面
根据上面的跳跃方法，写出BFS算法

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        black = set(forbidden)
        n = x + (a * b // math.gcd(a, b))  # 最大跳到x+（a与b的最小公倍数）处，再往前跳无法退回
        q, nextq = [], []
        forwarded = [False] * (n + 1)  # 记录向前跳过的位置，避免下次再次从已经向前跳过的位置向前跳
        backwarded = [False] * (n + 1)  # 同上
        q.append((0, False))
        forwarded[0] = True
        backwarded[0] = True
        ans = 0
        while q:
            i, allowBackward = q.pop()
            nexti = i + a
            if nexti <= n and nexti not in black and not forwarded[nexti]:  # 将向前能跳到的位置加入队列
                nextq.append((nexti, True))
                forwarded[nexti] = True
                if nexti == x:
                    return ans + 1
            if allowBackward:
                nexti = i - b
                if nexti > 0 and nexti not in black and not backwarded[nexti]:  # 将向后能跳到的位置加入队列
                    nextq.append((nexti, False))
                    backwarded[nexti] = True
                    if nexti == x:
                        return ans + 1
            if not q:
                q, nextq = nextq, q
                ans += 1
        return -1


s = Solution()
print(
    s.minimumJumps([
        162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64,
        122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98
    ], 29, 98, 80) == 121)
print(s.minimumJumps(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9))
print(s.minimumJumps(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11))
print(s.minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))

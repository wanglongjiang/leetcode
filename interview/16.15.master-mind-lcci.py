'''
面试题 16.15. 珠玑妙算
珠玑妙算游戏（the game of master mind）的玩法如下。

计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。
例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。
作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。
注意，“猜中”不能算入“伪猜中”。

给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。

示例：

输入： solution="RGBY",guess="GGRR"
输出： [1,1]
解释： 猜中1次，伪猜中1次。
提示：

len(solution) = len(guess) = 4
solution和guess仅包含"R","G","B","Y"这4种字符

'''
from typing import List
from collections import defaultdict
'''
思路：哈希计数
分别对2个字符串进行哈希计数，然后相同颜色的计数中取较小的值即为伪猜中

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        sc, gc = defaultdict(int), defaultdict(int)
        ans = [0, 0]
        for i in range(4):
            if solution[i] == guess[i]:
                ans[0] += 1
            else:
                sc[solution[i]] += 1
                gc[guess[i]] += 1
        for color in sc.keys():
            ans[1] += min(sc[color], gc[color])
        return ans

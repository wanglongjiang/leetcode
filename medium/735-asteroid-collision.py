'''
行星碰撞
给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸
两颗移动方向相同的行星，永远不会发生碰撞。

 

示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。

示例 3：
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

示例 4：
输入：asteroids = [-2,-1,1,2]
输出：[-2,-1,1,2]
解释：-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞
 

提示：

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
'''
from typing import List
'''
思路：栈
依次遍历asteroids，对于当前星球a，
1. 如果是正数，向右运动，由于不确定是否会碰碎，需要入栈
2. 如果是负数，向左运动，需要查看栈中是否有星球，如果有，需要出栈，再判断哪个星球会碎掉
    如果abs(a)>栈顶元素，需要持续将栈中的星球出栈，直至栈中的星球大于当前星球。
    或者栈为空（需要将该星球输出到结果中，因为该星球战胜了栈中所有星球）
时间复杂度：O(n)，每个元素最多入栈1次
空间复杂度：O(n)
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans, stack = [], []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] < -a:  # 向左运动的星球会击碎所有栈中<a的星球
                    stack.pop()
                if stack and stack[-1] == -a:  # 如果栈中星球与a势均力敌，2者湮灭
                    stack.pop()
                elif not stack:  # 星球打碎了所有栈中星球，输出到结果中
                    ans.append(a)
        # 栈中剩余的星球都是强者，需要输出到结果中
        ans.extend(stack)
        return ans


s = Solution()
print(s.asteroidCollision(asteroids=[5, 10, -5]))
print(s.asteroidCollision(asteroids=[8, -8]))
print(s.asteroidCollision(asteroids=[10, 2, -5]))
print(s.asteroidCollision(asteroids=[-2, -1, 1, 2]))

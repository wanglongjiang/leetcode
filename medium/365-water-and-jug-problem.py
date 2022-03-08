'''
365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False
'''
from collections import defaultdict
from collections import deque
'''
思路：BFS
x,y,z构成一个状态，用BFS遍历所有的状态，如果出现了z=targetCapacity，返回true
对于x,y,z，可能的下一个状态是x->0,x->full，x->min(x+y,jug1Capacity)
y->0,y->full，y->min(x+y,jug2Capacity)
详见代码注释
'''


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        marked = defaultdict(bool)
        marked[(0, 0, 0)] = True
        queue = deque()
        queue.append((0, 0, 0))
        while queue:
            x, y, z = queue.popleft()
            nextStatus = [(0, y), (jug1Capacity, y), (x, 0), (x, jug2Capacity)]  # x清空，x倒满，y清空，y倒满
            if x < jug1Capacity and y > 0:  # 将y倒入x
                newx = min(jug1Capacity, x + y)  # y有可能全部倒入或倒入一部分
                newy = y - (newx - x)  # y剩余的水
                nextStatus.append((newx, newy))
            if y < jug2Capacity and x > 0:  # 将x倒入y
                newy = min(jug2Capacity, x + y)  # x有可能全部倒入或倒入一部分
                newx = x - (newy - y)  # x剩余的水
                nextStatus.append((newx, newy))
            for newx, newy in nextStatus:  # 遍历所有的下一个状态
                if (newz := newx + newy) == targetCapacity:
                    return True
                if not marked[(newx, newy, newz)]:
                    marked[(newx, newy, newz)] = True
                    queue.append((newx, newy, newz))
        return False


s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(2, 6, 5))
print(s.canMeasureWater(1, 2, 3))
print(s.canMeasureWater(104579, 104593, 12444))

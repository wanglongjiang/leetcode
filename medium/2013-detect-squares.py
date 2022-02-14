'''
2013. 检测正方形
给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：

添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。

实现 DetectSquares 类：

DetectSquares() 使用空数据结构初始化对象
void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
 

示例：


输入：
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
输出：
[null, null, null, null, 1, 0, null, 2]

解释：
DetectSquares detectSquares = new DetectSquares()#
detectSquares.add([3, 10])#
detectSquares.add([11, 2])#
detectSquares.add([3, 2])#
detectSquares.count([11, 10])# // 返回 1 。你可以选择：
                               //   - 第一个，第二个，和第三个点
detectSquares.count([14, 8])#  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
detectSquares.add([11, 2])#    // 允许添加重复的点。
detectSquares.count([11, 10])# // 返回 2 。你可以选择：
                               //   - 第一个，第二个，和第三个点
                               //   - 第一个，第三个，和第四个点
 

提示：

point.length == 2
0 <= x, y <= 1000
调用 add 和 count 的 总次数 最多为 5000
'''
from typing import List
'''
思路：哈希
设一个哈希表，
add将所有的坐标保存到哈希表中
count会遍历哈希表中所有的坐标，如果与参数构成的边能够找到构成正方形的另外2个坐标，则将正方形数量+每个点的重复次数乘积

时间复杂度：add:O(1),count:O(n)
空间复杂度：O(n)
'''


class DetectSquares:
    def __init__(self):
        self.hash = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.hash:
            self.hash[(point[0], point[1])] = 0
        self.hash[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for key, val in self.hash.items():
            if key[0] != point[0]:  # 2个点构成的边与X轴、Y轴平行才符合题意，这里只取与y轴平行的一条边（垂直立着的边）
                continue
            cnt = 1
            cnt *= self.hash[(key[0], key[1])]  # 每个点可能有重复，构成的正方形数量需要相乘
            width = abs(key[1] - point[1])  # 正方形的边长
            if (key[0] - width, key[1]) in self.hash and (point[0] - width, point[1]) in self.hash:
                ans += cnt * self.hash[(key[0] - width, key[1])] * self.hash[(point[0] - width, point[1])]  # 累加与左边的点构成的正方形
            if (key[0] + width, key[1]) in self.hash and (point[0] + width, point[1]) in self.hash:
                ans += cnt * self.hash[(key[0] + width, key[1])] * self.hash[(point[0] + width, point[1])]  # 累加与右边的点构成的正方形
        return ans


detectSquares = DetectSquares()  #
detectSquares.add([3, 10])  #
detectSquares.add([11, 2])  #
detectSquares.add([3, 2])  #
print(detectSquares.count([11, 10]))  # // 返回 1 。你可以选择： 第一个，第二个，和第三个点
print(detectSquares.count([14, 8]))  #  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
detectSquares.add([11, 2])  #    // 允许添加重复的点。
print(detectSquares.count([11, 10]))  # // 返回 2 。你可以选择：
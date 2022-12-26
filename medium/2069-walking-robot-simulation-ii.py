'''
2069. 模拟行走机器人 II
给你一个在 XY 平面上的 width x height 的网格图，左下角 的格子为 (0, 0) ，右上角 的格子为 (width - 1, height - 1) 。
网格图中相邻格子为四个基本方向之一（"North"，"East"，"South" 和 "West"）。一个机器人 初始 在格子 (0, 0) ，方向为 "East" 。

机器人可以根据指令移动指定的 步数 。每一步，它可以执行以下操作。

沿着当前方向尝试 往前一步 。
如果机器人下一步将到达的格子 超出了边界 ，机器人会 逆时针 转 90 度，然后再尝试往前一步。
如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。

请你实现 Robot 类：

Robot(int width, int height) 初始化一个 width x height 的网格图，机器人初始在 (0, 0) ，方向朝 "East" 。
void move(int num) 给机器人下达前进 num 步的指令。
int[] getPos() 返回机器人当前所处的格子位置，用一个长度为 2 的数组 [x, y] 表示。
String getDir() 返回当前机器人的朝向，为 "North" ，"East" ，"South" 或者 "West" 。
 

示例 1：

example-1

输入：
["Robot", "move", "move", "getPos", "getDir", "move", "move", "move", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
输出：
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

解释：
Robot robot = new Robot(6, 3); // 初始化网格图，机器人在 (0, 0) ，朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (2, 0) ，并朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (4, 0) ，并朝东。
robot.getPos(); // 返回 [4, 0]
robot.getDir(); // 返回 "East"
robot.move(2);  // 朝东移动 1 步到达 (5, 0) ，并朝东。
                // 下一步继续往东移动将出界，所以逆时针转变方向朝北。
                // 然后，往北移动 1 步到达 (5, 1) ，并朝北。
robot.move(1);  // 朝北移动 1 步到达 (5, 2) ，并朝 北 （不是朝西）。
robot.move(4);  // 下一步继续往北移动将出界，所以逆时针转变方向朝西。
                // 然后，移动 4 步到 (1, 2) ，并朝西。
robot.getPos(); // 返回 [1, 2]
robot.getDir(); // 返回 "West"

 

提示：

2 <= width, height <= 100
1 <= num <= 105
move ，getPos 和 getDir 总共 调用次数不超过 104 次。
'''
from typing import List
'''
思路：设计
模拟题意进行设计。
设计一个函数数组，在一个方向上前进时，调用数组中的函数，得到剩余步数，循环调用，直至剩余步数为0

每一步操作时间复杂度都是O(1)
'''


class Robot:

    def __init__(self, width: int, height: int):
        self.x, self.y = 0, 0
        self.width, self.height = width, height
        self.dir = 0  # 4个方向分别是0，1，2，3
        self.dirs = ['East', 'North', 'West', 'South']  # 各个方向的名字

        # 向东走，到达边界停止，并返回剩余的步数
        def east(num):
            if self.x + num < self.width:
                self.x += num
                return 0
            num -= self.width - 1 - self.x
            self.x = self.width - 1
            return num

        # 向北走，到达边界停止，并返回剩余的步数
        def north(num):
            if self.y + num < self.height:
                self.y += num
                return 0
            num -= self.height - 1 - self.y
            self.y = self.height - 1
            return num

        # 向西走，到达边界停止，并返回剩余的步数
        def west(num):
            if self.x >= num:
                self.x -= num
                return 0
            num -= self.x
            self.x = 0
            return num

        # 向南走，到达边界停止，并返回剩余的步数
        def south(num):
            if self.y >= num:
                self.y -= num
                return 0
            num -= self.y
            self.y = 0
            return num

        self.go = [east, north, west, south]

    def step(self, num: int) -> None:
        num %= (self.width + self.height) << 1  # 超过一圈，取模
        while num := self.go[self.dir](num):  # 前进，直至把步数走完，最多循环4次
            self.dir = (self.dir + 1) & 0x3  # 改变方向

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dirs[self.dir]


s = Robot()
# [null,null,[6,10],"West",null,[7,1],"North",null,null,[4,10],"West",null,null,null,null,null,[0,2],"South",null,null,null,null,null,[2,10],"West",null,null,null,null,null,[0,4],"South",null,null,null,null,[1,10],"West",null,null,null]
# TODO

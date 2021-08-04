'''
模拟行走机器人
机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

-2 ：向左转 90 度
-1 ：向右转 90 度
1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。

返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）

 
注意：

北表示 +Y 方向。
东表示 +X 方向。
南表示 -Y 方向。
西表示 -X 方向。
 

示例 1：

输入：commands = [4,-1,3], obstacles = []
输出：25
解释：
机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 3 个单位，到达 (3, 4)
距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25
示例 2：

输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出：65
解释：机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
4. 左转
5. 向北走 4 个单位，到达 (1, 8)
距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65
 

提示：

1 <= commands.length <= 10^4
commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
0 <= obstacles.length <= 10^4
-3 * 10^4 <= xi, yi <= 3 * 10^4
答案保证小于 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walking-robot-simulation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：模拟
模拟指令的运行，中间记录最大的欧式距离的平方

时间复杂度：O(n),n=commands.length
空间复杂度：O(m),m=obstacles.length，需要将obstacles中的所有坐标加入哈希集合
'''


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        hashset = set(map(lambda x: (x[0], x[1]), obstacles))
        pos = (0, 0)
        ans = 0
        direct = 0  # 前进方向，0为北，1为东，2为南，3为西
        for cmd in commands:
            if cmd == -1:  # 右转
                direct = (direct + 1) % 4
            elif cmd == -2:  # 左转
                direct = 3 if direct == 0 else direct - 1
            else:
                for _ in range(cmd):  # 前进cmd步
                    if direct == 0:
                        newpos = (pos[0], pos[1] + 1)
                    elif direct == 1:
                        newpos = (pos[0] + 1, pos[1])
                    elif direct == 2:
                        newpos = (pos[0], pos[1] - 1)
                    else:
                        newpos = (pos[0] - 1, pos[1])
                    if newpos in hashset:
                        break
                    else:
                        pos = newpos
                        ans = max(ans, pos[0] * pos[0] + pos[1] * pos[1])
        return ans


s = Solution()
print(s.robotSim(commands=[4, -1, 3], obstacles=[]))
print(s.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))

'''
1496. 判断路径是否相交
给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。

机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。

如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。



示例 1：



输入：path = "NES"
输出：false
解释：该路径没有在任何位置相交。
示例 2：



输入：path = "NESWW"
输出：true
解释：该路径经过原点两次。


提示：

1 <= path.length <= 10^4
path 仅由 {'N', 'S', 'E', 'W} 中的字符组成
'''
'''
思路：模拟+哈希
模拟移动，用哈希集合记录所有经过的点，判断是否有重复的点即可。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        directs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        points = set()
        points.add((0, 0))
        for d in map(lambda c: directs[c], path):
            x, y = x + d[0], y + d[1]
            if (x, y) in points:
                return True
            points.add((x, y))
        return False


s = Solution()
print(s.isPathCrossing('NESWW'))
print(s.isPathCrossing('NES'))

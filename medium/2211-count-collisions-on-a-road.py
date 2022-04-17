'''
2211. 统计道路上的碰撞次数
在一条无限长的公路上有 n 辆汽车正在行驶。汽车按从左到右的顺序按从 0 到 n - 1 编号，每辆车都在一个 独特的 位置。

给你一个下标从 0 开始的字符串 directions ，长度为 n 。directions[i] 可以是 'L'、'R' 或 'S' 分别表示第 i 辆车是向 左 、向 右 或者 停留 在当前位置。每辆车移动时 速度相同 。

碰撞次数可以按下述方式计算：

当两辆移动方向 相反 的车相撞时，碰撞次数加 2 。
当一辆移动的车和一辆静止的车相撞时，碰撞次数加 1 。
碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。

返回在这条道路上发生的 碰撞总次数 。

 

示例 1：

输入：directions = "RLRSLL"
输出：5
解释：
将会在道路上发生的碰撞列出如下：
- 车 0 和车 1 会互相碰撞。由于它们按相反方向移动，碰撞数量变为 0 + 2 = 2 。
- 车 2 和车 3 会互相碰撞。由于 3 是静止的，碰撞数量变为 2 + 1 = 3 。
- 车 3 和车 4 会互相碰撞。由于 3 是静止的，碰撞数量变为 3 + 1 = 4 。
- 车 4 和车 5 会互相碰撞。在车 4 和车 3 碰撞之后，车 4 会待在碰撞位置，接着和车 5 碰撞。碰撞数量变为 4 + 1 = 5 。
因此，将会在道路上发生的碰撞总次数是 5 。
示例 2：

输入：directions = "LLRR"
输出：0
解释：
不存在会发生碰撞的车辆。因此，将会在道路上发生的碰撞总次数是 0 。
 

提示：

1 <= directions.length <= 105
directions[i] 的值为 'L'、'R' 或 'S'
'''
'''
思路：模拟
模拟题意，用3个变量stop,right,left记录3种状态的车
当遇到right的车，right+1，stop=0
当遇到left的车，判断是否有right或stop
    如果有right，碰撞次数+right+1，同时stop=1,right=0
    如果有stop,碰撞次数+1
    如果没有right和stop，跳过
当遇到stop，stop=1,碰撞次数+right,right = 0

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countCollisions(self, directions: str) -> int:
        stop, left, right = 0, 0, 0
        ans = 0
        for d in directions:
            if d == 'S':
                ans += right
                stop = 1
                right = 0
            elif d == 'R':
                stop = 0
                right += 1
            else:
                if right:
                    ans += right + 1
                    stop = 1
                    right = 0
                elif stop:
                    ans += 1
        return ans


s = Solution()
print(s.countCollisions("RLRSLL"))
print(s.countCollisions("LLRR"))

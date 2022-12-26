'''
2059. 转化数字的最小运算数
中等
38
相关企业
给你一个下标从 0 开始的整数数组 nums ，该数组由 互不相同 的数字组成。另给你两个整数 start 和 goal 。

整数 x 的值最开始设为 start ，你打算执行一些运算使 x 转化为 goal 。你可以对数字 x 重复执行下述运算：

如果 0 <= x <= 1000 ，那么，对于数组中的任一下标 i（0 <= i < nums.length），可以将 x 设为下述任一值：

x + nums[i]
x - nums[i]
x ^ nums[i]（按位异或 XOR）
注意，你可以按任意顺序使用每个 nums[i] 任意次。使 x 越过 0 <= x <= 1000 范围的运算同样可以生效，
但该该运算执行后将不能执行其他运算。

返回将 x = start 转化为 goal 的最小操作数；如果无法完成转化，则返回 -1 。

 

示例 1：

输入：nums = [2,4,12], start = 2, goal = 12
输出：2
解释：
可以按 2 → 14 → 12 的转化路径进行，只需执行下述 2 次运算：
- 2 + 12 = 14
- 14 - 2 = 12
示例 2：

输入：nums = [3,5,7], start = 0, goal = -4
输出：2
解释：
可以按 0 → 3 → -4 的转化路径进行，只需执行下述 2 次运算：
- 0 + 3 = 3
- 3 - 7 = -4
注意，最后一步运算使 x 超过范围 0 <= x <= 1000 ，但该运算仍然可以生效。
示例 3：

输入：nums = [2,8,16], start = 0, goal = 1
输出：-1
解释：
无法将 0 转化为 1
 

提示：

1 <= nums.length <= 1000
-109 <= nums[i], goal <= 109
0 <= start <= 1000
start != goal
nums 中的所有整数互不相同
'''
from collections import deque
from typing import List
'''
[TOC]

# 思路
BFS

# 解题方法
> 因为x可能的状态只有[0,1000]，所以可以用x与nums每个元素进行3种运算，计算后的新状态如果未遍历过，且在[0,1000]内，需要继续遍历
> 执行所有遍历，直至运算后能得到goal或者所有状态都被耗尽。

# 复杂度
- 时间复杂度: 
> $O(n^2)$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        marked = set()
        queue = deque()
        queue.append(start)
        ans = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                x = queue.popleft()
                for num in nums:
                    for newx in [x + num, x - num, x ^ num]:
                        if newx == goal:
                            return ans
                        if 0 <= newx <= 1000 and newx not in marked:
                            marked.add(newx)
                            queue.append(newx)
            ans += 1
        return -1


s = Solution()
print(s.minimumOperations(nums=[2, 4, 12], start=2, goal=12))
print(s.minimumOperations(nums=[3, 5, 7], start=0, goal=-4))
print(s.minimumOperations(nums=[2, 8, 16], start=0, goal=1))

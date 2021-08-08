'''
数组中两个数的最大异或值

给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。

进阶：你可以在 O(n) 的时间解决这个问题吗？

 

示例 1：

输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.
示例 2：

输入：nums = [0]
输出：0
示例 3：

输入：nums = [2,4]
输出：6
示例 4：

输入：nums = [8,10,2]
输出：10
示例 5：

输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127
 

提示：

1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 231 - 1
'''
from typing import List
'''
思路：贪心算法
高位的1价值大于所有低位的1，再根据公式：如果a^b=c，那么a^c=b
可以从高到低遍历每个数的每一位（遍历32次），
1. 将每个整数的前缀记录下来
2. 假设一个最大值：amax，
3. 然后根据公式：最大值^整数前缀=某个整数前缀 如果成立，那么假设成立，将其记录下来
4. 重复上面1.2.3,从高位到低位逐步增大amax的值


时间复杂度：O(n)
空间复杂度：O(n)，需要保存所有整数的前缀，最坏情况下是O(n)
'''


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for i in range(31, -1, -1):  # 遍历每一位
            mask = mask | (1 << i)
            s = set()
            for num in nums:  # 将每个整数的前缀添加到set中
                s.add(num & mask)
            amax = ans | (1 << i)  # 假定最大值。初始假定为高位的1，
            for prefix in s:  # 遍历所有的前缀
                if amax ^ prefix in s:  # 根据公式：如果a^b=c,那么a^c=b，如果假定的最大值^整数前缀，也在前缀集合中存在，那么该假定成立
                    ans = amax  # 将该假定记录下来，然后进入低一位继续尝试
                    break
        return ans

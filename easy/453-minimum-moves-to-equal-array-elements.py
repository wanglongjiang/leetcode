'''
453. 最小操作次数使数组元素相等
给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。



示例：

输入：
[1,2,3]
输出：
3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''
from typing import List
'''
思路：脑筋急转弯
每次使n-1个元素+1，相对来说就是1个元素-1，题意可以看成将所有大于min(nums)的数值减小到min(nums)需要的次数
需要变动的次数是sum-min*n

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

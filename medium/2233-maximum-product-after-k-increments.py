'''
2233. K 次增加后的最大乘积
给你一个非负整数数组 nums 和一个整数 k 。每次操作，你可以选择 nums 中 任一 元素并将它 增加 1 。

请你返回 至多 k 次操作后，能得到的 nums的 最大乘积 。由于答案可能很大，请你将答案对 109 + 7 取余后返回。

 

示例 1：

输入：nums = [0,4], k = 5
输出：20
解释：将第一个数增加 5 次。
得到 nums = [5, 4] ，乘积为 5 * 4 = 20 。
可以证明 20 是能得到的最大乘积，所以我们返回 20 。
存在其他增加 nums 的方法，也能得到最大乘积。
示例 2：

输入：nums = [6,3,3,2], k = 2
输出：216
解释：将第二个数增加 1 次，将第四个数增加 1 次。
得到 nums = [6, 4, 3, 3] ，乘积为 6 * 4 * 3 * 3 = 216 。
可以证明 216 是能得到的最大乘积，所以我们返回 216 。
存在其他增加 nums 的方法，也能得到最大乘积。
 

提示：

1 <= nums.length, k <= 105
0 <= nums[i] <= 106
'''
from functools import reduce
from heapq import heapify, heapreplace
from typing import List
'''
思路：堆 贪心
将数组加入堆，每次最小元素+1这样增加的乘积最大
时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(k):
            heapreplace(nums, nums[0] + 1)
        return reduce(lambda a, b: (a * b) % 1000000007, nums)

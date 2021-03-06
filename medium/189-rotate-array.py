'''
旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

 

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
'''
from typing import List
'''
思路1，辅助数组
用一个辅助数组，将n-k..n-1复制到辅助数组，将0-(n-k-1)的元素复制到
k-n，再将辅助数组赋值到0..k-1
时间复杂度：O(n)
空间复杂度：O(n)

思路2，看官方题解知道的，翻转数组
第1次全数组翻转
第2次翻转0..k
第3次翻转k..n
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        arr = [0] * k
        for i in range(n - k, n):
            arr[i - n + k] = nums[i]
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = arr[i]

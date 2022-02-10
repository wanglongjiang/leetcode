'''
1502. 判断能否形成等差数列
给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
示例 2：

输入：arr = [1,2,4]
输出：false
解释：无法通过重新排序得到等差数列。
 

提示：

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
'''
from typing import List

from numpy import true_divide
'''
思路：哈希
将所有元素加入哈希表，然后用最大值-最小值/元素个数得到差，如果从最小值开始累加的数值在哈希中都存在，则是等差数列

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        hashset = set()
        maxVal, minVal = float('-inf'), float('inf')
        for val in arr:
            hashset.add(val)
            maxVal = max(maxVal, val)
            minVal = min(minVal, val)
        d = (maxVal - minVal) // (len(arr) - 1)
        if d == 0:
            return True
        for val in range(minVal + d, maxVal, d):
            if val not in hashset:
                return False
        return True

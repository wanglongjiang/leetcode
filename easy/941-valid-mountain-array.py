'''
有效的山脉数组
给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

arr.length >= 3
在 0 < i < arr.length - 1 条件下，存在 i 使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
 



 

示例 1：

输入：arr = [2,1]
输出：false
示例 2：

输入：arr = [3,5,5]
输出：false
示例 3：

输入：arr = [0,3,2,1]
输出：true
 

提示：

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：模拟
按照山脉数组的定义，从小到大，从大到小。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i + 1] > arr[i]:  # 上坡，直至i到达峰顶
            i += 1
        if i == 0:  # 顶点前必须有小于顶点的
            return False
        while i + 1 < n:  # 下坡
            if arr[i + 1] >= arr[i]:
                return False
            i += 1
        return True

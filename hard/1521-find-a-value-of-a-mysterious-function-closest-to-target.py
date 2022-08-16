'''
1521. 找到最接近目标值的函数值


Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，
他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。

请你返回 |func(arr, l, r) - target| 的最小值。

请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。

 

示例 1：

输入：arr = [9,12,3,7,15], target = 5
输出：2
解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。
示例 2：

输入：arr = [1000000,1000000,1000000], target = 1
输出：999999
解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
示例 3：

输入：arr = [1,2,4,8,16], target = 0
输出：0
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
0 <= target <= 10^7
'''
import operator
from functools import reduce
from typing import List
'''
思路：位运算
针对每个arr[i]，其与左侧的子数组按位与只会越来越小，可能的按位与的结果有log(arr[i])种
arr[i+1]与左侧子数组的和，实际上可以重复利用arr[i]与左侧子数组的按位与的集合。

时间复杂度：O(nlog(max(arr)))
空间复杂度：O(log(max(arr)))
'''


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = abs(arr[0] - target)
        andResults = {arr[0]}
        for num in arr:
            andResults = {num & andResult for andResult in andResults} | {num}
            ans = min(ans, min(abs(andResult - target) for andResult in andResults))
        return ans

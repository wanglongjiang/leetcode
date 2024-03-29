'''
1346. 检查整数及其两倍数是否存在
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

示例 1：

输入：arr = [10,2,5,3]
输出：true
解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。
示例 2：

输入：arr = [7,1,14,11]
输出：true
解释：N = 14 是 M = 7 的两倍，即 14 = 2 * 7 。
示例 3：

输入：arr = [3,1,7,11]
输出：false
解释：在该情况下不存在 N 和 M 满足 N = 2 * M 。
 

提示：

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
'''

from typing import List
'''
思路：哈希
将所有整数加入哈希
然后再次遍历数组，查找其二倍是否在哈希表中
需要对0进行特殊处理

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        zeroCount = 0
        for i in arr:
            if i == 0:
                zeroCount += 1
                if zeroCount > 1:
                    return True
            elif i * 2 in s:
                return True
        return False


s = Solution()
print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))

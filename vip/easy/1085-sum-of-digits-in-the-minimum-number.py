'''
1085. 最小元素各数位之和
给你一个正整数的数组 A。

然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。

最后，假如 S 所得计算结果是 奇数 ，返回 0 ；否则请返回 1。



示例 1:

输入：[34,23,1,24,75,33,54,8]
输出：0
解释：
最小元素为 1 ，该元素各个数位上的数字之和 S = 1 ，是奇数所以答案为 0 。
示例 2：

输入：[99,77,33,66,55]
输出：1
解释：
最小元素为 33 ，该元素各个数位上的数字之和 S = 3 + 3 = 6 ，是偶数所以答案为 1 。


提示：

1 <= A.length <= 100
1 <= A[i] <= 100
'''
from typing import List
'''
思路：数学
找到最小值，求其各位上的数字之和，然后判断奇偶

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        num = min(nums)
        s = 0
        while num:
            num, r = divmod(num, 10)
            s += r
        return 0 if s % 2 else 1


s = Solution()
print(s.sumOfDigits([34, 23, 1, 24, 75, 33, 54, 8]))
print(s.sumOfDigits([99, 77, 33, 66, 55]))

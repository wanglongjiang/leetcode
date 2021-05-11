'''
子数组的最小值之和

给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

 

示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。


示例 2：

输入：arr = [11,81,94,43,3]
输出：444
 

提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
'''
from typing import List
'''
思路：单调栈
使用单调递增栈，将arr中数据入栈，如果发生出栈，需要计算出栈的元素在多少个子数组中出现
为简化计算，需要使用哨兵
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        A = [0] + arr + [0]  # 为简化算法，使用哨兵，确保边界有值和清空栈
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:  # 栈顶元素遇到更小的元素，出栈，并计算栈顶元素在多少个子数组中是最小值
                j = stack.pop()
                k = stack[-1]  # 上一个入栈的元素j-k为距离上一个入栈元素的数组大小
                ans += A[j] * (i - j) * (j - k)  # 当前出栈的元素，在(i-j)*(j-k)个子数组中作为最小值出现过
            stack.append(i)
        return ans % (10**9 + 7)  # 结果取模


s = Solution()
print(s.sumSubarrayMins([3, 1, 2, 4]))
print(s.sumSubarrayMins([11, 81, 94, 43, 3]))

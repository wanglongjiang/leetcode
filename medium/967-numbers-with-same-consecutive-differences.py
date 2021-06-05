'''
连续差相同的数字
返回所有长度为 n 且满足其每两个连续位上的数字之间的差的绝对值为 k 的 非负整数 。

请注意，除了 数字 0 本身之外，答案中的每个数字都 不能 有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 3, k = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。
示例 2：

输入：n = 2, k = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
示例 3：

输入：n = 2, k = 0
输出：[11,22,33,44,55,66,77,88,99]
示例 4：

输入：n = 2, k = 2
输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
 

提示：

2 <= n <= 9
0 <= k <= 9
'''
from typing import List
'''
思路：回溯
第1个数尝试从1变化到9，后面的数根据前面的数进行等差变化
时间复杂度：O(10^n)
空间复杂度：O(n)
'''


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        nums = []

        def backtrack(num):
            nums.append(num)
            if len(nums) == n:  # 已经够了n位数，输出到结果list
                ans.append(nums[0])
                for i in range(1, n):
                    ans[-1] = ans[-1] * 10 + nums[i]
                nums.pop()
                return
            if num - k >= 0:  # 剪枝，如果k为0，+0-0相同，需要跳过；下一个数必须大于等于0
                backtrack(num - k)
            if k > 0 and num + k < 10:  # 剪枝，下一个数必须小于10
                backtrack(num + k)
            nums.pop()

        for i in range(1, 10):
            if i + k < 10 or i - k >= 0:  # 剪枝，下一个数必须介于0和9
                backtrack(i)
        return ans


s = Solution()
print(s.numsSameConsecDiff(n=2, k=1) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98])
print(s.numsSameConsecDiff(n=3, k=7) == [181, 292, 707, 818, 929])
print(s.numsSameConsecDiff(n=2, k=0) == [11, 22, 33, 44, 55, 66, 77, 88, 99])
print(s.numsSameConsecDiff(n=2, k=2) == [13, 20, 24, 31, 35, 42, 46, 53, 57, 64, 68, 75, 79, 86, 97])

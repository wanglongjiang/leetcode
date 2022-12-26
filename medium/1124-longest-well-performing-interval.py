'''
表现良好的最长时间段
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。

 

示例 1：

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
 

提示：

1 <= hours.length <= 10000
0 <= hours[i] <= 16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-well-performing-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
以输入样例 hours = [9,9,6,0,6,6,9] 为例，我们将大于 88 小时的一天记为 11 分，小于等于 88 小时的一天记为 -1−1 分。
那么处理后，我们得到 score = [1, 1, -1, -1, -1, -1, 1]，然后我们对得分数组计算前缀和 presum = [0, 1, 2, 1, 0, -1, -2, -1]。
题目要求返回表现良好时间段的最大长度，即求最长的一段中，得分 11 的个数大于得分 -1−1 的个数，也就是求 score 数组中最长的一段子数组，
其和大于 00，那么也就是找出前缀和数组 presum 中两个索引 i 和 j，使 j - i 最大，
且保证 presum[j] - presum[i] 大于 00。
到此，我们就将这道题转化为，求 presum 数组中的一个最长的上坡，可以用单调栈实现。
我们维护一个单调栈，其中存储 presum 中的元素索引，栈中索引指向的元素严格单调递减，
由 presum 数组求得单调栈为 stack = [0, 5, 6]， 其表示元素为 [0, -1, -2]。然后我们从后往前遍历 presum 数组，
与栈顶索引指向元素比较，如果相减结果大于 00，则一直出栈，直到不大于 00 为止，然后更新当前最大宽度。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        # 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        # 倒序扫描数组，求最大长度坡
        i = n
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans


s = Solution()
assert s.longestWPI([6, 6, 9]) == 1
print(s.longestWPI([9, 9, 6, 0, 6, 6, 9]))

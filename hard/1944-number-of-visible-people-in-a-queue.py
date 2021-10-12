'''
1944. 队列中可以看到的人数
有 n 个人排成一个队列，从左到右 编号为 0 到 n - 1 。给你以一个整数数组 heights ，每个整数 互不相同，heights[i] 表示第 i 个人的高度。

一个人能 看到 他右边另一个人的条件是这两人之间的所有人都比他们两人 矮 。更正式的，
第 i 个人能看到第 j 个人的条件是 i < j 且 min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]) 。

请你返回一个长度为 n 的数组 answer ，其中 answer[i] 是第 i 个人在他右侧队列中能 看到 的 人数 。



示例 1：



输入：heights = [10,6,8,5,11,9]
输出：[3,1,2,1,1,0]
解释：
第 0 个人能看到编号为 1 ，2 和 4 的人。
第 1 个人能看到编号为 2 的人。
第 2 个人能看到编号为 3 和 4 的人。
第 3 个人能看到编号为 4 的人。
第 4 个人能看到编号为 5 的人。
第 5 个人谁也看不到因为他右边没人。
示例 2：

输入：heights = [5,1,2,3,10]
输出：[4,1,1,1,0]


提示：

n == heights.length
1 <= n <= 10^5
1 <= heights[i] <= 10^5
heights 中所有数 互不相同 。
'''

from typing import List
'''
思路：单调栈
设一个答案数组ans，一个栈stk，栈中存放下标，栈中的下标指向的高度是单调递减的。
初始将下标0入栈。
遍历heights（从1开始），对于当前元素heights[i]，
如果大于栈顶元素，那么i和栈顶元素j互相能看见，j能看到的数量+1，即ans[j]+=1。
此后j不能再看见i后面的元素了，因为height[i]>height[j]，j也不能看到j之前的元素，因为单调栈中保存的数据性质保证了这一点，可以将j出栈。
持续上面过程，直至栈顶元素大于i，将i入栈，同时比i大的那个元素也能看到i，需要+1

时间复杂度：O(n)，整个数组遍历一次，每个元素最多入栈一次
空间复杂度：O(n)
'''


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        stk = [0]
        for i in range(1, len(heights)):
            while stk and heights[stk[-1]] < heights[i]:
                ans[stk.pop()] += 1  # 栈内小于i的元素，它与i元素之间的元素肯定小于i或者不存在，所以它能看到i
            if stk:
                ans[stk[-1]] += 1  # 栈顶第1个大于i的元素，可以看到i
            stk.append(i)
        return ans


s = Solution()
print(s.canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(s.canSeePersonsCount([5, 1, 2, 3, 10]))

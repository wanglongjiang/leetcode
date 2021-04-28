'''
每日温度

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''
from typing import List
'''
思路：单调栈
将T[0]入栈，然后遍历整个温度数值T[1..n-1]：
    如果当前温度t[i]<=栈顶温度，入栈
    如果当前温度t[i]>栈顶温度，栈顶元素j出栈，j需要的天数为i-j
    持续上面的过程2，直至栈顶元素>=当前温度，然后将当前温度入栈

时间复杂度：O(n)，每个元素最多入栈1次
空间复杂度：O(n)，每个元素最多入栈1次
'''


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        while not stack:
            ans[stack.pop()] = 0
        return ans


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

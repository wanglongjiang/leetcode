'''
跳跃游戏 V
给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：

i + x ，其中 i + x < arr.length 且 0 < x <= d 。
i - x ，其中 i - x >= 0 且 0 < x <= d 。
除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，
其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。

你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。

请注意，任何时刻你都不能跳到数组的外面。

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
'''
from typing import List
'''
思路：DFS+动态规划
用深度优先搜索从i开始所有路径，返回路径最长的一个。
时间复杂度：O(n*n)
空间复杂度：O(n)
'''


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        jumpLen = [1] * n  # 每个节点默认都能跳1下（自身）
        marked = [False] * n

        def dfs(i):
            marked[i] = True
            # 向左跳
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] < arr[i]:  # 只有可以跳过去的才进行后续处理
                    if marked[j]:  # 这个路径已经DFS遍历过，从i跳到j的最大深度为jumpLen[j]+1
                        jumpLen[i] = max(jumpLen[i], jumpLen[j] + 1)
                    else:  # 如果未遍历，进行遍历
                        jumpLen[i] = max(jumpLen[i], dfs(j) + 1)
                else:  # 遇到第1个高于arr[i]的元素之后，后面的都不能再跳过去了
                    break
            # 向右跳
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] < arr[i]:  # 只有可以跳过去的才进行后续处理
                    if marked[j]:  # 这个路径已经DFS遍历过，从i跳到j的最大深度为jumpLen[j]+1
                        jumpLen[i] = max(jumpLen[i], jumpLen[j] + 1)
                    else:  # 如果未遍历，进行遍历
                        jumpLen[i] = max(jumpLen[i], dfs(j) + 1)
                else:  # 遇到第1个高于arr[i]的元素之后，后面的都不能再跳过去了
                    break
            return jumpLen[i]

        maxJump = 0
        for i in range(n):
            maxJump = max(maxJump, dfs(i))
        return maxJump


s = Solution()
print(s.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))  # 4
print(s.maxJumps(arr=[3, 3, 3, 3, 3], d=3))  # 1
print(s.maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1))  # 7
print(s.maxJumps(arr=[7, 1, 7, 1, 7, 1], d=2))  # 2
print(s.maxJumps(arr=[66], d=1))  # 1

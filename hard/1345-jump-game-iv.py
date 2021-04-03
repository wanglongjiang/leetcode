'''
跳跃游戏 IV
给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 i 跳到下标：

i + 1 满足：i + 1 < arr.length
i - 1 满足：i - 1 >= 0
j 满足：arr[i] == arr[j] 且 i != j
请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

注意：任何时候你都不能跳到数组外面。

提示：

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
'''
from typing import List
'''
思路：BFS
广度优先搜索。每个点有3个路径可以走：左、右、相同值，搜索最快到达终点坐标的路径数即可。
1、首先遍历一次数组，将所有相同的元素放到同一个集合中
2、用BFS搜索最短路径。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if n > 1 and arr[0] == arr[-1]:
            return 1
        sameItem = {}
        # 1、统计相同元素坐标
        for i in range(n):
            if arr[i] in sameItem:
                sameItem[arr[i]].append(i)
            else:
                sameItem[arr[i]] = [i]
        # 2、用BFS搜索最短路径
        import collections
        queue = collections.deque()
        queue.append(0)  # -1为每层的哨兵
        queue.append(-1)
        marked = [False] * n
        step = 0
        while len(queue) > 0:
            i = queue.popleft()
            if i < 0:
                queue.append(-1)
                step += 1
                continue
            if i == n - 1:
                return step
            marked[i] = True
            if arr[i] in sameItem:  # 添加相同值的路径
                sameIndexs = sameItem[arr[i]]
                del sameItem[arr[i]]  # 相同的值只遍历一次，避免重复遍历
                for j in range(len(sameIndexs) - 1, -1, -1):
                    sameIndex = sameIndexs[j]
                    if not marked[sameIndex]:
                        queue.append(sameIndex)
            right = i + 1  # 添加向右的路径
            if right < n and not marked[right]:
                queue.append(right)
            left = i - 1  # 添加向左的路径
            if left >= 0 and not marked[left]:
                queue.append(left)


s = Solution()
print(s.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
print(s.minJumps([7]))
print(s.minJumps([7, 6, 9, 6, 9, 6, 9, 7]))
print(s.minJumps([6, 1, 9]))
print(s.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))

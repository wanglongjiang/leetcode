'''
跳跃游戏 III
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，
你可以跳到 i + arr[i] 或者 i - arr[i]。

请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。

'''
from typing import List
'''
思路：BFS
广度遍历。如果遍历过程中遇到值为0的元素，返回true。如果从start开始的路径全部遍历完，还未跳到值为0的元素，返回false。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        import collections
        queue = collections.deque()
        n = len(arr)
        marked = [False] * n
        queue.append(start)
        while len(queue) > 0:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            marked[i] = True
            left = i - arr[i]
            if left >= 0 and not marked[left]:
                queue.append(left)
            right = i + arr[i]
            if right < n and not marked[right]:
                queue.append(right)
        return False


s = Solution()
print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(s.canReach(arr=[3, 0, 2, 1, 2], start=2))

'''
滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''
from typing import List
from collections import deque
'''
思路1：TreeMap
使用java里面的TreeMap维护窗口内的有序集合，每次取最大值
时间复杂度：O(nlogk)
空间复杂度：O(k)

思路2：单调队列
设一个队列queue，内部只能递减。
遍历nums，
> nums[j]为要移出窗口的元素，如果nums[i]==queue[0]时，queue[0]可以出队。
> nums[i]为要进入窗口的元素，当nums[i]>queue[-1]时，queue[-1]可以抛弃，因为窗口中最大值肯定不是queue[-1]。持续改过程，直至队列为空或者queue[-1]>=nums[i]

时间复杂度：O(n)
空间复杂度：O(k)
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        j = 0
        ans = [q[0]]
        for i in range(k, len(nums)):
            if nums[j] == q[0]:
                q.popleft()
            j += 1
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans


s = Solution()
print(s.maxSlidingWindow(nums=[1], k=1))
print(s.maxSlidingWindow(nums=[1, -1], k=1))
print(s.maxSlidingWindow(nums=[9, 11], k=2))
print(s.maxSlidingWindow(nums=[4, -2], k=2))

'''
找出最具竞争力的子序列
给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。

数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。

在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。

 

示例 1：

输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
示例 2：

输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]
 

提示：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= nums.length
'''
from typing import List
from collections import deque
'''
思路：队列
对于一个大小为k的子序列，如果有nums[i]>nums[i+1]，且子序列后面还有元素，那么nums[i+1]替换nums[i]在队列中的位置，新的元素添加到队尾，子序列会更有竞争力。
根据上面的思路，可以用一个大小为k的队列，找到队列中第1个q[i]>q[i+1]的地方，q[i]删除，然后将新的元素加入队尾。
如果队列中找不到q[i]>q[i+1]，队尾元素与新元素对比，如果队尾大于新元素，删除队尾，将新元素加入队尾。
持续上面的过程，直至数组所有元素都遍历完。

复杂度：
> 时间复杂度：O(n)
> 空间复杂度：O(n)
'''


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return [min(nums)]
        if k == len(nums):
            return nums
        # 将前k个元素加入队列
        q = deque(nums[:k])
        n, i = len(nums), k
        while i < n:
            p = 1
            while p < k and q[p] >= q[p - 1]:  # 找到队列中第1个出现变小的地方
                p += 1
            if p == k:  # 队列为单调递增，只需要对比队尾
                while i < n:
                    if q[k - 1] > nums[i]:  # 找到小于队尾的元素
                        q.pop()  # 将第1个小于队尾的元素替换队尾
                        q.append(nums[i])
                        if q[k - 2] > q[k - 1]:  # 如果队列不再是单调递增，退出循环
                            p = k - 1
                            i += 1
                            break
                    i += 1
            # 新的元素加入队列，删除p-1指向的出现递减的元素
            while i < n and p > 0 and q[p] < q[p - 1]:
                del q[p - 1]
                p -= 1
                q.append(nums[i])
                i += 1
        return list(q)


s = Solution()
print(s.mostCompetitive(nums=[3, 5, 2, 6], k=2))
print(s.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))

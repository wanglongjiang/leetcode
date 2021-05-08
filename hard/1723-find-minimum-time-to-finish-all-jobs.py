'''
完成所有工作的最短时间
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间
是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。

 

示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
 

提示：

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
'''
from typing import List
'''
思路1，回溯+剪枝
尝试将数组中的时间依次加到每个工人的任务时间里

时间复杂度：<O(n!)
空间复杂度：O(n)
'''


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        bags = [0] * k
        n = len(jobs)
        ans = float('inf')

        def backtrack(index):
            nonlocal ans
            if index == n:
                ans = min(ans, max(bags))
                return
            for i in range(k):
                if bags[i] + jobs[index] >= ans:  # 剪枝，将大于以往最大答案的跳过
                    continue
                bags[i] += jobs[index]
                backtrack(index + 1)
                bags[i] -= jobs[index]
                if bags[i] == 0:  # 剪枝，跳过当前工人未分配任务的组合
                    break

        backtrack(0)
        return ans


s = Solution()
print(s.minimumTimeRequired([9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365, 3758448, 9881935, 2420271, 4542202], 9))
print(s.minimumTimeRequired([12, 13, 14, 17, 25], 3))
print(s.minimumTimeRequired([5, 5, 4, 4, 4], 2))
print(s.minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))
print(s.minimumTimeRequired(jobs=[3, 2, 3], k=3))

'''
用户分组

有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组 groupSizes，
其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。

你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。

提示：

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
'''
from typing import List
'''
思路：哈希
设置一个哈希表，key为用户组大小，val为用户组list。相同用户组大小的用户以贪心模式加入list，如果list已满，从哈希表中移出。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        mp = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in mp:
                mp[groupSizes[i]].append(i)
                if len(mp[groupSizes[i]]) == groupSizes[i]:
                    ans.append(mp.pop(groupSizes[i]))
            else:
                if groupSizes[i] == 1:
                    ans.append([i])
                else:
                    mp[groupSizes[i]] = [i]
        return ans


s = Solution()
print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople([2, 1, 3, 3, 3, 2]))

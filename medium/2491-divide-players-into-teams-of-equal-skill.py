'''
2491. 划分技能点相等的团队
中等
3
相关企业
给你一个正整数数组 skill ，数组长度为 偶数 n ，其中 skill[i] 表示第 i 个玩家的技能点。
将所有玩家分成 n / 2 个 2 人团队，使每一个团队的技能点之和 相等 。

团队的 化学反应 等于团队中玩家的技能点 乘积 。

返回所有团队的 化学反应 之和，如果无法使每个团队的技能点之和相等，则返回 -1 。

 

示例 1：

输入：skill = [3,2,5,1,3,4]
输出：22
解释：
将玩家分成 3 个团队 (1, 5), (2, 4), (3, 3) ，每个团队的技能点之和都是 6 。
所有团队的化学反应之和是 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22 。
示例 2：

输入：skill = [3,4]
输出：12
解释：
两个玩家形成一个团队，技能点之和是 7 。
团队的化学反应是 3 * 4 = 12 。
示例 3：

输入：skill = [1,1,2,3]
输出：-1
解释：
无法将玩家分成每个团队技能点都相等的若干个 2 人团队。
 

提示：

2 <= skill.length <= 105
skill.length 是偶数
1 <= skill[i] <= 1000
'''
from collections import defaultdict
from typing import List
'''
[TOC]

# 思路
哈希

# 解题方法
首先，计算整个数组的和total，total/(n/2)即为每个团队的技能和，设其为ssum

然后，遍历skill，如果ssum-skill[i]在哈希表中存在，那么这2个数字可以组成一个团队。否则将其加入哈希表。

最后，如果所有数字都能组成数对，则返回所有数对乘积的和。

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ssum, r = divmod(sum(skill), len(skill) // 2)
        if r:
            return -1
        ans = 0
        counter = defaultdict(int)
        for num in skill:
            if ssum - num in counter:
                counter[ssum - num] -= 1
                ans += num * (ssum - num)
                if counter[ssum - num] == 0:
                    del counter[ssum - num]
            else:
                counter[num] += 1
        return ans if len(counter) == 0 else -1


s = Solution()
assert s.dividePlayers([2, 3, 4, 2, 5, 5]) == 32

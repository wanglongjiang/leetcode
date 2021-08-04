'''
表现良好的最长时间段
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。

 

示例 1：

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
 

提示：

1 <= hours.length <= 10000
0 <= hours[i] <= 16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-well-performing-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路1，前缀和+哈希
设变量sums为前缀和，遍历hours数组：
> 当hours[i]>8时，sums-1
> 当hours[i]<=8时，sums+1
当sums>=0时，还达不到表现良好，需要将(sums,i)作为key,val记录到哈希表hashset中。
> 保存sums之前，先要判断hashset中有没有与Sums相同的key，如果存在，说明在之前某个坐标j不劳累的天数与当前坐标相同。
> 那么从坐标j到坐标i，劳累的天数肯定大于不劳累的天数。需要记录此时的表现良好的天数。
当sums<0时，从0到i，表现良好，需要记录天数

时间复杂度：O(n)，一次遍历
空间复杂度：O(n)，需要哈希表记录所有的sums>=0
'''


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hashset = {}
        ans, sums = 0, 0
        for i, h in enumerate(hours):
            sums += -1 if h > 8 else 1
            if sums < 0:
                ans = i + 1  # 当前前缀和小于0，从0..i都是表现良好
            else:
                if sums in hashset:  # 如果存在与当前坐标相同的前缀和，意味着坐标j=hashset[sums]与当前坐标i的不劳累天数相同，减去0..j的天数，剩下的j+1..i就是表现良好的
                    ans = max(ans, i - hashset[sums])
                else:
                    hashset[sums] = i
        return ans


s = Solution()
print(s.longestWPI([9, 9, 6, 0, 6, 6, 9]))

'''
救生艇
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

 

示例 1：
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)

示例 2：
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)

示例 3：
输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)

提示：
1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
'''
from typing import List
'''
思路：排序+双指针
> 1. 排序
> 2. 设2个指针left,right分别指向数组的2端，然后尝试将left,right指向的元素组合到一起，
>> 如果和>limit，right指向的元素没有配对的，需要单独输出，right指针向左移动
>> 如果和<=limit，left,right指针都向内移动

复杂度：
> 时间复杂度：O(nlogn)，排序需要O(nlogn)，第2步需要O(n)
> 空间复杂度：O(1)
'''


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans


s = Solution()
print(s.numRescueBoats(people=[1, 2], limit=3))
print(s.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(s.numRescueBoats(people=[3, 5, 3, 4], limit=5))

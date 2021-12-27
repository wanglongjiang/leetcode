'''
825. 适龄的朋友
人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。

当满足以下任一条件时，A 不能给 B（A、B不为同一人）发送好友请求：

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
否则，A 可以给 B 发送好友请求。

注意如果 A 向 B 发出了请求，不等于 B 也一定会向 A 发出请求。而且，人们不会给自己发送好友请求。

求总共会发出多少份好友请求?



示例 1：

输入：[16,16]
输出：2
解释：二人可以互发好友申请。
示例 2：

输入：[16,17,18]
输出：2
解释：好友请求可产生于 17 -> 16, 18 -> 17.
示例 3：

输入：[20,30,100,110,120]
输出：3
解释：好友请求可产生于 110 -> 100, 120 -> 110, 120 -> 100.


提示：

1 <= ages.length <= 20000
1 <= ages[i] <= 120
'''
from typing import List
'''
思路：排序 双指针
从题意中知道，a只能向与自己同岁或比自己略小的人发送申请。
首先，对数组进行排序
然后，设left,right指针，初始指向0
从小到大遍历每个人,设当前值为ages[i]，right指针向右移动到>ages[i]，left指针向右移动到满足>0.5*ages[i]+7
此时left,right之间的差即为可以发送好友的数量（需要减去自身）


时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        left, right = 0, 0
        ans = 0
        for a in ages:
            while left < n and ages[left] <= 0.5 * a + 7:  # 移动left指针，提升交友下限
                left += 1
            while right < n and ages[right] <= a:  # 移动right指针，提升交友上限
                right += 1
            if right - left > 1:
                ans += right - left - 1
        return ans


s = Solution()
print(s.numFriendRequests([16, 16]))
print(s.numFriendRequests([16, 17, 18]))
print(s.numFriendRequests([20, 30, 100, 110, 120]))

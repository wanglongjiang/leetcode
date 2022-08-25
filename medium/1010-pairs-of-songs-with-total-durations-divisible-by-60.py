'''
1010. 总持续时间可被 60 整除的歌曲
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

 

示例 1：

输入：time = [30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整除：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：

输入：time = [60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整除。
 

提示：

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
'''
from math import factorial
from typing import Counter, List
'''
思路：哈希
1、遍历time，统计所有时间的个数
2、2重循环遍历不同的时间，如果2个时间之和为60的整数倍，记录这2个时间构成的数对个数。
如果2个时间不同，数对个数为2个时间的个数的乘积；如果2个时间相同，数对个数为n!/2*(n-2)!

时间复杂度：O(n+m^2)，m为time中不同整数的个数
空间复杂度：O(m)
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = Counter(time)
        nums = list(count.keys())
        ans = 0
        for i in range(len(nums)):
            if count[nums[i]] > 1 and nums[i] % 30 == 0:
                ans += factorial(count[nums[i]]) // (2 * factorial(count[nums[i]] - 2))
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) % 60 == 0:
                    ans += count[nums[i]] * count[nums[j]]
        return ans

'''
2354. 优质数对的数目
给你一个下标从 0 开始的正整数数组 nums 和一个正整数 k 。

如果满足下述条件，则数对 (num1, num2) 是 优质数对 ：

num1 和 num2 都 在数组 nums 中存在。
num1 OR num2 和 num1 AND num2 的二进制表示中值为 1 的位数之和大于等于 k ，其中 OR 是按位 或 操作，而 AND 是按位 与 操作。
返回 不同 优质数对的数目。

如果 a != c 或者 b != d ，则认为 (a, b) 和 (c, d) 是不同的两个数对。例如，(1, 2) 和 (2, 1) 不同。

注意：如果 num1 在数组中至少出现 一次 ，则满足 num1 == num2 的数对 (num1, num2) 也可以是优质数对。

 

示例 1：

输入：nums = [1,2,3,1], k = 3
输出：5
解释：有如下几个优质数对：
- (3, 3)：(3 AND 3) 和 (3 OR 3) 的二进制表示都等于 (11) 。值为 1 的位数和等于 2 + 2 = 4 ，大于等于 k = 3 。
- (2, 3) 和 (3, 2)： (2 AND 3) 的二进制表示等于 (10) ，(2 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
- (1, 3) 和 (3, 1)： (1 AND 3) 的二进制表示等于 (01) ，(1 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
所以优质数对的数目是 5 。
示例 2：

输入：nums = [5,1,1], k = 10
输出：0
解释：该数组中不存在优质数对。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 60
'''
from typing import Counter, List
'''
思路：位运算
a and b，a or b 的位数和，实际上就是bitcount(a)+bitcount(b)。
bitcount(x)最多有30种，
遍历一次nums（需要去重），将bitcount(x)放到哈希表中计数，然后用一个二重循环计算符合题意的数对个数

时间复杂度：O(n+count^2)，其中count<=30
空间复杂度：O(count)
'''


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(num.bit_count() for num in set(nums))
        ans = 0
        for bitcountx, numcountx in counter.items():
            for bitcounty, numcounty in counter.items():
                if bitcountx + bitcounty >= k:
                    ans += numcountx * numcounty
        return ans

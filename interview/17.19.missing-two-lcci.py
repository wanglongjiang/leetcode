'''
面试题 17.19. 消失的两个数字
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]
示例 2:

输入: [2,3]
输出: [1,4]
提示：

nums.length <= 30000
'''
from typing import List
from functools import reduce
'''
思路1，哈希表
将nums所有数据加入哈希表，然后遍历1.n的整数，如果不存在于哈希表的2个整数找出来
时间复杂度：O(n)
空间复杂度：O(n)

思路2，分治法
利用快排里面的分治方法，随机选择pivot，将数据分成>pivot和<pivot的2个区，
> 如果2个区都缺少一个整数。每个区都使用异或得到缺少的数。
> 如果只有1个区缺少2个数，继续进行分治。最后如果有1个区大小为2，数据全部在这1个区里面，那么就能根据与pivot的关系得到2个数字了。
时间复杂度：O(n)
空间复杂度：O(1)

思路3，数学 位运算
整个数组进行异或，然后再与1..n进行异或，得到的结果就是缺少的2个数字的异或xor。
再求整个数组的和total，然后1..n的和-total得到2个数字的和s。
将s分解成2个整数，如果2个整数的异或与xor相同，则找到2个数字的候选，为了排除有异或相同的一对数字，需要再判定一下数字是否在数组中存在。
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路3， 数学+位运算
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        xor = reduce(lambda a, b: a ^ b, nums) ^ reduce(lambda a, b: a ^ b, range(1, n + 1))
        twoSum = sum(range(1, n + 1)) - sum(nums)
        for a in range(1, twoSum // 2 + 1):
            if a ^ (twoSum - a) == xor and nums.count(a) == 0:
                return [a, twoSum - a]
        return []


s = Solution()
print(s.missingTwo([1]))
print(s.missingTwo([2, 3]))

'''
2165. 重排数字的最小值
给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。

返回不含前导零且值最小的重排数字。

注意，重排各位数字后，num 的符号不会改变。

 

示例 1：

输入：num = 310
输出：103
解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。
不含任何前导零且值最小的重排数字是 103 。
示例 2：

输入：num = -7605
输出：-7650
解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
不含任何前导零且值最小的重排数字是 -7650 。
 

提示：

-10^15 <= num <= 10^15
'''
'''
思路：排序、贪心
将构成num的所有数字进行排序，
    如果是正数，从小到大重组成数字，0插入到第1个非0数字后面
    如果是负数，从大到小重组成数字，0插入到所有非0数字后面

时间复杂度：O(logn^2)
空间复杂度：O(logn)
'''


class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num:
            return num
        neg = False
        if num < 0:
            neg = True
            num = -num
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums.sort()
        zeroCount = 0
        for v in nums:
            if not v:
                zeroCount += 1
            else:
                break
        if neg:
            for v in reversed(nums[zeroCount:len(nums)]):
                num = num * 10 + v
            for i in range(zeroCount):
                num *= 10
            num = -num
        else:
            nums[0], nums[zeroCount] = nums[zeroCount], nums[0]
            for i in range(len(nums)):
                num = num * 10 + nums[i]
        return num


s = Solution()
print(s.smallestNumber(310))
print(s.smallestNumber(-7605))

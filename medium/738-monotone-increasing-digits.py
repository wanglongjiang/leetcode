'''
738. 单调递增的数字
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
'''
'''
思路：贪心 数学
首先，将整数n转为数组nums。
然后，从高位到低位遍历每位数字，寻找第1个出现下降的数字，
> 如果找到nums[i-1]>nums[i]，其中i-1是高位，i是低位，
> 那么，可以从i-1借一位给i位，i及后面的数字都变成9,nums[i-1]需要减去1。
> 当nums[i-1]减去1之后，比nums[i-2]小，需要继续从i-2借一位，nums[i-1]变成9。
> 持续上面的借位过程，直至高位不再小于低位。

时间复杂度：O($log^n$)
空间复杂度：O($log^n$)
'''


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = []
        while n:  # 将数字拆分成数组
            n, r = divmod(n, 10)
            nums.append(r)
        nums.reverse()  # 从左到右为从高位到低位
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:  # 出现高位大于低位，需要开始借位
                nums[i - 1] -= 1
                for j in range(i, len(nums)):  # i及以后的数字都变成9
                    nums[j] = 9
                j = i - 1
                while j - 1 >= 0 and nums[j] < nums[j - 1]:  # 向高位遍历，如果出现借位后高位小于低位，需要持续借位
                    nums[j] = 9
                    nums[j - 1] -= 1
                    j = j - 1
                break
        for num in nums:  # 将数组合并成数字
            n = n * 10 + num
        return n


s = Solution()
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(110))
print(s.monotoneIncreasingDigits(121))
print(s.monotoneIncreasingDigits(150))
print(s.monotoneIncreasingDigits(55554))

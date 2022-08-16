'''
670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 10^8]
'''
'''
思路：贪心 数学
高位的数字找到低位里面比它大，而且是最大的数字进行交换

时间复杂度：O(logn)
空间复杂度：O(logn)
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = []
        while num:
            num, r = divmod(num, 10)
            nums.append(r)
        nums.reverse()
        for i in range(len(nums)):
            maxIdx = i
            for j in range(i + 1, len(nums)):  # 在低位里面找比当前位大最多的数字
                if nums[j] > nums[maxIdx]:
                    maxIdx = j
            if maxIdx != i:  # 如果找到了，交换到高位，中止循环
                nums[i], nums[maxIdx] = nums[maxIdx], nums[i]
                break
        for i in range(len(nums)):
            num = num * 10 + nums[i]
        return num


s = Solution()
print(s.maximumSwap(2736))
print(s.maximumSwap(9973))
print(s.maximumSwap(9937))

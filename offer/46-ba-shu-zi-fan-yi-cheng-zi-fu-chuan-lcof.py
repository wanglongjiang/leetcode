'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231
'''
'''
思路：动态规划
将num转化为数字序列nums，没有前导0
设动态规划数组dp，dp[i]的意思是截止数字i的转化数量
> 当nums[0]不为0时，dp[0]为1
> 当nums[0..1]>25时，dp[1]为1
> 当nums[0..1]<25，且不为10，20时，dp[1]为2
经过上面的分析，得到状态转移方程：
dp[i] = dp[i-1]，此时nums[i-1..i]>25 或者 nums[i-1]==0
dp[i] = 0 ，此时nums[i-1..i]==0
dp[i] = dp[i-2]+dp[i-1]，此时0<nums[i-1..i]<=25

与- 91.[解码方法](medium/91-decode-ways.py) 类似

时间复杂度：O(1)，num中整数个数是log10(2^31)
空间复杂度：O(1)
'''


class Solution:
    def translateNum(self, num: int) -> int:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums.reverse()
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        if n == 1:
            return 1
        else:
            num = nums[0] * 10 + nums[1]
            if num > 25:
                dp[1] = 1
            else:
                dp[1] = 2
        for i in range(2, n):
            twoBit = nums[i - 1] * 10 + nums[i]
            if twoBit > 25 or nums[i - 1] == 0:  # >25，=10，=20的情况下，只有一种选择，不会对解码数量造成影响
                dp[i] = dp[i - 1]
            else:  # 这种情况下nums[i]可以与nums[i-1]结合，解码数量为dp[i-2]；或者不与nums[i-1]结合，解码数量为dp[i-1]。两个相加即为总的解码数
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


s = Solution()
print(s.translateNum(220))
print(s.translateNum(506))
print(s.translateNum(26))
print(s.translateNum(12258))
print(s.translateNum(12))
print(s.translateNum(225))

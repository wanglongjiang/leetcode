'''
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。



示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1


提示：

1 <= n <= 2^31 - 1
'''
'''
思路：数学 排序
如果从右到左的数字是一个递增序列，那么不存在这样的正整数。
如果不满足上面的条件，设第1个出现降序的位置为i，也就是nums[i]<nums[i+1]
需要从i+1..n-1中找到第1个大于nums[i]的数字，将其交换到nums[i]，然后nums[i+1..n-1]再升序
上面的nums是从高位到低位排列的，下面的代码中进行了颠倒，nums中的数字从低位到高位排列

时间复杂度：O($log^n$)
空间复杂度：O($log^n$)
'''


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n:
            n, r = divmod(n, 10)
            nums.append(r)  # 从地位到高位，放入数组
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  # 出现了高位比低位数字小
                j = i - 1  # j指向的数字大于nums[i]
                for k in range(i - 1):  # 这个迭代寻找比nums[i]大，比nums[j]小的索引
                    if nums[i] < nums[k] < nums[j]:
                        j = k
                nums[i], nums[j] = nums[j], nums[i]  # 将找到的最接近nums[i]的数字与nums[i]进行交换，这样序列已经比n大
                lowRange = nums[:i]
                lowRange.sort(reverse=True)  # i之前的数字从低位到高位要升序排列
                nums = lowRange + nums[i:]
                break
        else:  # 整个序列都是升序，返回-1
            return -1
        for i in range(len(nums) - 1, -1, -1):  # 把数组拼接成整数
            n = n * 10 + nums[i]
        return n if n <= (1 << 31) - 1 else -1


s = Solution()
print(s.nextGreaterElement(2147483476))
print(s.nextGreaterElement(12))
print(s.nextGreaterElement(21))
print(s.nextGreaterElement(3254331))

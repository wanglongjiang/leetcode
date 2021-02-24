'''
排列序列
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

'''
'''
思路：回溯
设置一个1-n的数组，对其进行回溯排列，直至回溯到第K个排列
回溯时需要注意，将1个元素从数组中提取出来后，剩余的元素要保证顺序正确
时间复杂度：O(n!*n)
空间复杂度：O(n)
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        self.k = k
        self.ans = None

        def backtrack(index: int):
            if index == n - 1:
                self.k -= 1
                if self.k == 0:
                    self.ans = ''.join(map(str, nums))
            for i in range(index, n):
                if i - index == 1:  # 第2个元素需要交换
                    nums[i], nums[index] = nums[index], nums[i]
                elif i - index > 1:  # 第3个元素开始，才会出现顺序不对，需要把剩余的元素顺序重新梳理
                    num = nums[i]
                    for j in range(i, index, -1):
                        nums[j] = nums[j - 1]
                    nums[index] = num
                backtrack(index + 1)
                if self.k == 0:
                    break
                if i - index == 1:  # 第2个元素交换的需要恢复
                    nums[i], nums[index] = nums[index], nums[i]
                elif i - index > 1:  # 第3个元素元素顺序恢复
                    num = nums[index]
                    for j in range(index, i):
                        nums[j] = nums[j + 1]
                    nums[i] = num

        backtrack(0)
        return self.ans


s = Solution()
print(s.getPermutation(4, 24))

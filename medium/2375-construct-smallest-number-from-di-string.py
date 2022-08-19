'''
2375. 根据模式串构造最小数字
给你下标从 0 开始、长度为 n 的字符串 pattern ，它包含两种字符，'I' 表示 上升 ，'D' 表示 下降 。

你需要构造一个下标从 0 开始长度为 n + 1 的字符串，且它要满足以下条件：

num 包含数字 '1' 到 '9' ，其中每个数字 至多 使用一次。
如果 pattern[i] == 'I' ，那么 num[i] < num[i + 1] 。
如果 pattern[i] == 'D' ，那么 num[i] > num[i + 1] 。
请你返回满足上述条件字典序 最小 的字符串 num。

 

示例 1：

输入：pattern = "IIIDIDDD"
输出："123549876"
解释：
下标 0 ，1 ，2 和 4 处，我们需要使 num[i] < num[i+1] 。
下标 3 ，5 ，6 和 7 处，我们需要使 num[i] > num[i+1] 。
一些可能的 num 的值为 "245639871" ，"135749862" 和 "123849765" 。
"123549876" 是满足条件最小的数字。
注意，"123414321" 不是可行解因为数字 '1' 使用次数超过 1 次。
示例 2：

输入：pattern = "DDD"
输出："4321"
解释：
一些可能的 num 的值为 "9876" ，"7321" 和 "8742" 。
"4321" 是满足条件最小的数字。
 

提示：

1 <= pattern.length <= 8
pattern 只包含字符 'I' 和 'D' 。
'''
'''
思路：回溯
回溯生成所有数字的排列，找到满足条件最小的数字

时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums, n = [str(i) for i in range(1, len(pattern) + 2)], len(pattern) + 1
        ans = float('inf')

        def backtrack(i, nums):
            nonlocal ans
            if i == n - 1:
                ans = min(int(''.join(nums)), ans)
                return
            for j in range(i + 1, n):
                if (pattern[i] == 'I' and nums[i] < nums[j]) or (pattern[i] == 'D' and nums[i] > nums[j]):  # 剪枝，只执行匹配的模式
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]  # 第j个字符排到i后面满足要求，将其位置进行更换
                    backtrack(i + 1, nums)
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]  # 还原变动

        for i in range(0, n):
            nums[0], nums[i] = nums[i], nums[0]  # 将一个数字排到第0个位置上
            backtrack(0, nums)
            nums[0], nums[i] = nums[i], nums[0]  # 还原更改
        return str(ans)


s = Solution()
print(s.smallestNumber("DDD"))
print(s.smallestNumber("IIIDIDDD"))

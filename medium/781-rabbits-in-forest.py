'''
森林中的兔子
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。

返回森林中兔子的最少数量。
示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0
说明:

answers 的长度最大为1000。
answers[i] 是在 [0, 999] 范围内的整数。
'''
from typing import List
'''
思路：一次遍历。（官方给这个思路叫贪心算法）
一个兔子说的数字是除自己以外的兔子数量n，那么跟这个兔子同色的兔子共n+1只，n一共会出现n+1次。
故每个数字如果不满足数字n出现n+1次，需要补足n+1。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nums = {}
        # 统计每个数字出现的次数
        for a in answers:
            if a in nums:
                nums[a] += 1
            else:
                nums[a] = 1
        count = len(answers)  # 兔子的总数量
        for num, c in nums.items():
            d, r = divmod(c, num + 1)
            if r > 0:
                count += num + 1 - r  # 如果数字出现的次数不是num+1的整数倍，缺少的兔子需要补充
        return count


s = Solution()
print(s.numRabbits([1, 1, 2]))
print(s.numRabbits([10, 10, 10]))
print(s.numRabbits([]))

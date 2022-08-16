'''
646. 最长数对链
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。



示例：

输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]


提示：

给出数对的个数在 [1, 1000] 范围内。
'''
from typing import List
'''
思路：排序 动态规划
1. 对pairs进行排序
2. 进行动态规划：设dp[n]，dp[i]意思是pairs[i]能构成的最大数对链长度，状态转移方程为
dp[i] = max(dp[j]+1)，j满足0<=j<i，且pairs[j][1]<pairs[i][0]

时间复杂度：O($n^2$)
空间复杂度：O(n)
'''


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                elif dp[i] > j:  # 剪枝，如果链的长度已经超过索引，前面的索引不需要再遍历
                    break
        return dp[-1]


s = Solution()
print(s.findLongestChain([[1, 2], [2, 3], [3, 4]]))

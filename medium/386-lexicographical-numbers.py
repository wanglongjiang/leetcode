'''
字典序排数
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographical-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：DFS
遍历1..9的数字，
> 对于当前数字i，尝试将其乘以10后+0..9即a=i*10+[0..9]，如果a<=n，将a加入结果，然后递归尝试将a增加1位

时间复杂度：O(n)
空间复杂度：O(logn)
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(i):
            i *= 10
            for j in range(10):
                if i + j <= n:
                    ans.append(i + j)
                    if (i + j) * 10 <= n:
                        dfs(i + j)

        for i in range(1, min(10, n + 1)):
            ans.append(i)
            dfs(i)
        return ans


s = Solution()
print(s.lexicalOrder(13))

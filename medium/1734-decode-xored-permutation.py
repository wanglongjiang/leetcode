'''
解码异或后的排列

给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，
如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

 

示例 1：

输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
示例 2：

输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]
 

提示：

3 <= n < 10^5
n 是奇数。
encoded.length == n - 1
'''
from typing import List
'''
思路：异或
异或
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        ans = [0] * (n + 1)
        prefix = [0] * (n)
        prefix[0] = encoded[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ encoded[i]
        tmp = 0
        for i in range(n):
            tmp ^= prefix[i]
        allnum = 0
        for i in range(1, n + 2):
            allnum ^= i
        ans[0] = allnum ^ tmp
        for i in range(1, n + 1):
            ans[i] = ans[i - 1] ^ encoded[i - 1]
        return ans


s = Solution()
print(s.decode([3, 1]))
print(s.decode([6, 5, 4, 6]))

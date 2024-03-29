'''
2438. 二的幂数组中查询范围内的乘积
给你一个正整数 n ，你需要找到一个下标从 0 开始的数组 powers ，它包含 最少 数目的 2 的幂，且它们的和为 n 。powers 数组是 非递减 顺序的。根据前面描述，构造 powers 数组的方法是唯一的。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] ，其中 queries[i] 表示请你求出满足 lefti <= j <= righti 的所有 powers[j] 的乘积。

请你返回一个数组 answers ，长度与 queries 的长度相同，其中 answers[i]是第 i 个查询的答案。由于查询的结果可能非常大，请你将每个 answers[i] 都对 109 + 7 取余 。

 

示例 1：

输入：n = 15, queries = [[0,1],[2,2],[0,3]]
输出：[2,4,64]
解释：
对于 n = 15 ，得到 powers = [1,2,4,8] 。没法得到元素数目更少的数组。
第 1 个查询的答案：powers[0] * powers[1] = 1 * 2 = 2 。
第 2 个查询的答案：powers[2] = 4 。
第 3 个查询的答案：powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64 。
每个答案对 109 + 7 得到的结果都相同，所以返回 [2,4,64] 。
示例 2：

输入：n = 2, queries = [[0,0]]
输出：[2]
解释：
对于 n = 2, powers = [2] 。
唯一一个查询的答案是 powers[0] = 2 。答案对 109 + 7 取余后结果相同，所以返回 [2] 。
 

提示：

1 <= n <= 109
1 <= queries.length <= 105
0 <= starti <= endi < powers.length
'''
import itertools
from typing import List
'''
思路：位运算 前缀和
首先，找到构成n的指数，使用移位得到这一数组。
然后，求出指数数组的前缀和。
最后，遍历queries，对于queries[i]，它实际上是求指数数组的区间和，然后计算出2的指数，这个时候可以用到第2步计算出的前缀和数组。


时间复杂度：O(log(n)+m)，m=len(queries)
空间复杂度：O(log(n))
'''


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 计算出构成n的指数数组
        indexs = []
        i = 0
        while n:
            if n & 1:
                indexs.append(i)
            n >>= 1
            i += 1
        # 计算指数数组的前缀和
        pres = list(itertools.accumulate(indexs))
        # 计算答案
        ans, mod = [], 10**9 + 7
        for q in queries:
            ans.append((1 << (pres[q[1]] if q[0] == 0 else pres[q[1]] - pres[q[0] - 1])) % mod)
        return ans


s = Solution()
print(s.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]))
print(s.productQueries(n=2, queries=[[0, 0]]))

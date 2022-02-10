'''
1447. 最简分数
给你一个整数 n ,请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

 

示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]
示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数,因为它可以化简为 "1/2" 。
示例 4：

输入：n = 1
输出：[]
 

提示：

1 <= n <= 100
'''

from http.client import OK
from typing import List
'''
数学：遍历所有的分子、分母组合,然后查看分子分母是否能同时被同一素数整除
用gcd算法复杂度还能再降一点

时间复杂度：O(n^3)
空间复杂度：O(1)
'''


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for a in range(2, n + 1):  # 分母
            for b in range(1, a):  # 分子
                ok = True
                for p in primes:
                    if p > b:
                        break
                    if a % p == 0 and b % p == 0:
                        ok = False
                        break
                if ok:
                    ans.append(str(b) + "/" + str(a))
        return ans

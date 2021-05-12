'''
子数组异或查询

有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。

对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。

并返回一个包含给定查询 queries 所有结果的数组。

 

示例 1：

输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8]
解释：
数组中元素的二进制表示形式是：
1 = 0001
3 = 0011
4 = 0100
8 = 1000
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8
示例 2：

输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]
 

提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length
'''
from typing import List
'''
思路：前缀数组
根据异或性质，(a^b^c^d)^(a^b)=c^d，可以设一个前缀异或数组xorArr
xorArr[0]=0
xorArr[i]=arr[0]^arr[1]^...arr[i]
对于queries[i] = [Li, Ri]，xorArr[Li]=arr[0]^...arr[Li],xorArr[Ri]=arr[0]^...arr[Li]...arr[Ri]
xorArr[Li]^xorArr[Ri] = arr[Li+1]^...arr[Ri]
所以，结果ans[i] = xorArr[Li]^xorArr[Ri]^arr[Li]

时间复杂度：O(n+m)，n=arr.length, m = queries.length
空间复杂度：O(n)
'''


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xorArr = [0] * n
        xorArr[0] = arr[0]
        for i in range(1, n):
            xorArr[i] = xorArr[i - 1] ^ arr[i]
        xorArr[0] = 0
        ans = []
        for q in queries:
            if q[0] == q[1]:  # 特殊处理Li==Ri的情况
                ans.append(arr[q[0]])
            elif q[0] == 0:  # 从0开始，不需要异或前缀
                ans.append(xorArr[q[1]])
            else:
                ans.append(xorArr[q[0]] ^ xorArr[q[1]] ^ arr[q[0]])
        return ans


s = Solution()
print(s.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
print(s.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))

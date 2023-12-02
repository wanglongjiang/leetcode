from typing import List
'''
[TOC]

# 思路
数组遍历

# 解题方法
由于每次操作只会改变1个元素的颜色，所以只需要查看其相邻元素颜色

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n+l)$
'''


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(n)]
        ans = [0 for _ in range(len(queries))]
        colors = 0
        for i, q in enumerate(queries):
            if q[1] != arr[q[0]]:
                if q[0] > 0:
                    if q[1] == arr[q[0] - 1]:
                        colors += 1
                    elif arr[q[0]] == arr[q[0] - 1] and arr[q[0]] != 0:
                        colors -= 1
                if q[0] < n - 1:
                    if q[1] == arr[q[0] + 1]:
                        colors += 1
                    elif arr[q[0]] == arr[q[0] + 1] and arr[q[0]] != 0:
                        colors -= 1
                arr[q[0]] = q[1]
            ans[i] = colors
        return ans

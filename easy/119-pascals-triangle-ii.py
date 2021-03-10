'''
杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
'''

from typing import List
'''
思路：数学公式。杨辉三角的第n行的第1个数为1，第二个数为1*(n-1)，第三个数为1*(n-1)*(n-2)/2，第四个数为1*(n-1)*(n-2)/2*(n-3)/3…依此类推。
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        ans = [1] * n
        q, r = divmod(n, 2)  # 前半部分计算，后半部分复制
        for i in range(1, q + r):
            ans[i] = ans[i - 1] * (n - i) // i

        for i in range(q, n - 1):
            ans[i] = ans[n - i - 1]
        return ans


s = Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
print(s.getRow(6))

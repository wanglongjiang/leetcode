'''
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
'''
from typing import List
'''
思路：前缀数组
从左到右计算前缀乘积数组prefix，再从右到左计算后缀积数组postfix
然后答案ans[i] = prefix[i-1]*postfix[i+1]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        prefix, postfix, ans = [0] * n, [0] * n, [0] * n
        prefix[0] = a[0]
        postfix[-1] = a[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * a[i]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * a[i]
        ans[0], ans[-1] = postfix[1], prefix[-2]
        for i in range(1, n - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        return ans

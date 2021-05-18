'''
形成两个异或相等数组的三元组数目
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

 

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8
 

提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
'''
from typing import List
'''
思路：位运算
根据a^(a^b)=b的性质，求3元组的子串异或，就是求2个子数组的异或，可以将数组的异或前缀保存到前缀数组prefix中。
判断三元组是否成立为判断：prefix[i-1]^prefix[j-1]==prefix[j-1]^prefix[k]是否成立
又，如果a=b那么，a^b=0，故上面的公式可以简化为prefix[i-1]^prefix[k]==0，只需满足这个条件，这个子数组内的j任意拆分都是0即子数组长度-1

时间复杂度：O(n^2)，需要2重的循环，迭代所有的前缀子数组
空间复杂度：O(n)
'''


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        # 求异或前缀
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        # 遍历每个子数组异或是否为0，如果为0，则它的任意2个非空子数组都是合法三元组
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if i == 0 and prefix[j] == 0:
                    ans += j
                elif i > 0 and prefix[i - 1] ^ prefix[j] == 0:
                    ans += j - i
        return ans


s = Solution()
print(s.countTriplets([2, 3, 1, 6, 7]))
print(s.countTriplets([1, 1, 1, 1, 1]))
print(s.countTriplets([2, 3]))
print(s.countTriplets([1, 3, 5, 7, 9]))
print(s.countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))

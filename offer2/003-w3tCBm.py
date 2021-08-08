'''
剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

 

示例 1:

输入: n = 2
输出: [0,1,1]
解释:
0 --> 0
1 --> 1
2 --> 10
示例 2:

输入: n = 5
输出: [0,1,1,2,1,2]
解释:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

说明 :

0 <= n <= 10^5
 

进阶:

给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描做到吗？
要求算法的空间复杂度为 O(n) 。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount ）来执行此操作。
 

注意：本题与主站 338 题相同：https://leetcode-cn.com/problems/counting-bits/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/w3tCBm
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：动态规划
根据位运算的技巧n&(n-1)能够消掉最低位的1，故n&(n-1)比n少1个1，而且n&(n-1)比n小，
得到动态规划状态转移方程：
ans[n]=ans[n&(n-1)]+1

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans

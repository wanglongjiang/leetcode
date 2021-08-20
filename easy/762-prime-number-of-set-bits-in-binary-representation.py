'''
二进制表示中质数个计算置位
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:

输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
示例 2:

输入: L = 10, R = 15
输出: 5
解释:
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
注意:

L, R 是 L <= R 且在 [1, 10^6] 中的整数。
R - L 的最大值为 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：位运算 哈希
l,r最大值是10^6，所以最多用2^21表示，判断质数可以将21以内的质数放入哈希集合中
遍历从l到r的所有整数，对为1的位计数，判断是否在质数集合中

时间复杂度：O(nlogn)，对1个整数计数它含有的1需要O(logn)的时间
空间复杂度：O(1)
'''


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for num in range(left, right + 1):
            count = 0
            while num:
                num &= num - 1  # 小技巧，n&(n-1)能够消掉最低位的1
                count += 1
            if count in prime:
                ans += 1
        return ans
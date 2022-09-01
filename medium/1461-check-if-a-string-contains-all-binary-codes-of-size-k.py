'''
1461. 检查一个字符串是否包含所有长度为 K 的二进制子串
给你一个二进制字符串 s 和一个整数 k 。如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 true ，否则请返回 false 。

 

示例 1：

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
示例 2：

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
示例 3：

输入：s = "0110", k = 2
输出：false
解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
 

提示：

1 <= s.length <= 5 * 105
s[i] 不是'0' 就是 '1'
1 <= k <= 20
'''
'''
思路：位运算 哈希
设一个滑动窗口，将长度为k的子串依次加入哈希表。
如果哈希表的大小为2^k，说明所有k的子串都在s内，否则有不在s内的

时间复杂度：O(n)
空间复杂度：O(2^k)
'''


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) - k + 1 < 2**k:
            return False
        num = int(s[:k], 2)
        mask, bitset = 0, {num}
        # 初始化掩码
        for _ in range(k):
            mask = (mask << 1) | 1
        # 将所有的子串形成的数字加入哈希表
        for i in range(k, len(s)):
            num = ((num << 1) | int(s[i])) & mask
            bitset.add(num)
        return len(bitset) == 2**k

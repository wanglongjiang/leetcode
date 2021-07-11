'''
找出最长的超赞子字符串
给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

该字符串是 s 的一个非空子字符串
进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 

示例 1：

输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
示例 2：

输入：s = "12345678"
输出：1
示例 3：

输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
示例 4：

输入：s = "00"
输出：2
 

提示：

1 <= s.length <= 10^5
s 仅由数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-longest-awesome-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：哈希 位运算
回文串里面的字符，要么每个字符个数都是偶数，要么只有1个字符个数是奇数。
可以用10bit来表示每个数字出现的是奇数还是偶数。
统计每个索引处的前缀字符串的字符奇偶数a，如果a为0或者只有1bit为1，则为回文串。
如果a中有多个bit为1，依次将各个bit为1的屏蔽掉，如果剩余的数字在之前出现过，说明该字符串减去某一个前缀能成为回文。

时间复杂度：O(n),n=s.length
空间复杂度：O(n)
'''


class Solution:
    def longestAwesome(self, s: str) -> int:
        prefixMap = {}  # 用于记录前缀出现的索引
        prefix = 0
        ans = 0
        for i, c in enumerate(s):
            prefix ^= 1 << int(c)
            if prefix == 0 or prefix & (prefix - 1) == 0:  # 每个字符都是偶数，或者只有1个字符出现了奇数次，是回文串
                ans = i + 1
            else:
                for j in range(10):
                    mask = 1 << j
                    if prefix & ~mask:  # 依次遍历每个为1的bit
                        if prefix ^ mask in prefixMap:  # 将该bit置为0之后，如果出现在prefixMap里面，说明当前字符串减去找到的前缀只有1个bit为1，是回文串
                            ans = max(ans, i - prefixMap[prefix ^ mask])
            if prefix not in prefixMap:
                prefixMap[prefix] = i  # 将前缀加入哈希表，且只加入最早出现的那个
        return ans


s = Solution()
print(s.longestAwesome('3242415'))
print(s.longestAwesome('12345678'))
print(s.longestAwesome('213123'))
print(s.longestAwesome('00'))

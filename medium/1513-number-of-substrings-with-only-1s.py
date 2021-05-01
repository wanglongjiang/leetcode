'''
仅含 1 的子串数
给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。

返回所有字符都为 1 的子字符串的数目。

由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

提示：

s[i] == '0' 或 s[i] == '1'
1 <= s.length <= 10^5
'''
'''
思路：数学
通过观察看出，连续的1形成的长度为n的字符串其子字符串为：
长度n:1个
长度n-1:2个
长度n-2:3个
..
长度1:n个

所以，一个长度n的连续字符串，其内部子字符串的数目是1+2+3..+n=(n+1)n/2
可以将字符串转为连续1构成的长度的数组，比如1110001111可以转为[3,4]
再求长度数组的子串数量之和
时间复杂度：O(n)
空间复杂度：O(n)

'''


class Solution:
    def numSub(self, s: str) -> int:
        nums = []
        pre = '0'
        count = 0
        # 1、遍历求出连续1的子串长度
        for c in s:
            if c == '1' and pre == '1':
                count += 1
            elif c == '1':
                count = 1
                pre = '1'
            else:
                pre = '0'
                if count > 0:
                    nums.append(count)
        if count > 0:
            nums.append(count)
        # 2、求子串数量之和
        total = 0
        for n in nums:
            total += (n + 1) * n // 2
        return total % (10**9 + 7)


s = Solution()
print(s.numSub("0110111"))
print(s.numSub("101"))
print(s.numSub("111111"))
print(s.numSub("000"))

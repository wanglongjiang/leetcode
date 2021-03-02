'''
复原 IP 地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
'''
from typing import List
'''
思路：双指针法
左边指针从下标1开始，右边指针从n-1开始，中间指针依次遍历中间位置
每变动一次位置，判断是否合法ip
'''


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return False

        def isValidIp(*params):
            for p in params:
                if len(p) > 1 and p[0] == '0':
                    return False
                if int(p) > 255:
                    return False
            return True

        left = 1
        ans = []
        while left < 4 and left + 3 <= n:
            right = n - 1
            while right > left + 1 and right >= n - 3:
                for mid in range(left + 1, right):
                    if left > 3:
                        break
                    if mid - left > 3:
                        continue
                    if right - mid > 3:
                        continue
                    p1, p2, p3, p4 = s[0:left], s[left:mid], s[mid:right], s[right:]
                    if isValidIp(p1, p2, p3, p4):
                        ans.append(p1 + '.' + p2 + '.' + p3 + '.' + p4)
                right -= 1
            left += 1
        return ans


s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("0000"))
print(s.restoreIpAddresses("1111"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("101023"))

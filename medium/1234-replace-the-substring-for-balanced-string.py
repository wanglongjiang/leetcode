'''
替换子串得到平衡字符串
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

 

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 0。

 

示例 1：

输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：

输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
示例 3：

输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。
示例 4：

输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
 

提示：

1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符
'''
from collections import Counter
'''
思路：滑动窗口
1. 首先对4个字符分别计数，超过s.length/4的需要被替换成其他字符，将其记录到counter中
2. 然后用滑动窗口遍历s，如果窗口内字符串>=counter中的，记录此时的子串长度

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        need = Counter(s)  # 存放需要替换的字符计数
        for c in ['Q', 'W', 'E', 'R']:
            if need[c] <= target:  # <=target的字符不需要替换，删除计数器
                del need[c]
            else:
                need[c] -= target  # >target的字符需要替换
        if not need:
            return 0
        counter = Counter()
        left, right = 0, 0
        ans = float('inf')
        while right < n:
            windowOk = True
            for char, count in need.items():
                if counter[char] < need[char]:  # 如果窗口中的字符不满足需要替换的数量，将windowOk标记置为false
                    windowOk = False
                    break
            if windowOk:  # 窗口满足要求，记录此时的最小子字符串长度，然后缩小窗口
                ans = min(ans, right - left)
                counter[s[left]] -= 1
                left += 1
            else:  # 窗口不满足要求，扩大窗口大小
                counter[s[right]] += 1
                right += 1
        return ans


s = Solution()
print(s.balancedString("WWEQERQWQWWRWWERQWEQ"))
print(s.balancedString('QWER'))
print(s.balancedString('QQWE'))
print(s.balancedString('QQQW'))
print(s.balancedString('QQQQ'))

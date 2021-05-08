'''
串联字符串的最大长度

给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。

请返回所有可行解 s 中最长长度。

 

示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。
示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
 

提示：

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] 中只含有小写英文字母
'''
from typing import List
'''
思路：信息压缩+回溯
回溯求所有字符串的组合，如果组合中没有重复的字符，返回其长度
时间复杂度：<O(n!)
空间复杂度：O(n)
'''


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        nums = []
        lens = [len(s) for s in arr]
        maxlens = [0] * n
        maxlens[-1] = lens[-1]
        for i in range(n - 2, -1, -1):
            maxlens[i] = maxlens[i + 1] + lens[i]
        # 信息压缩，将每个字符表示为1位，每个字符串表示为1个整数，如果字符串中有重复字符，设置为-1
        for s in arr:
            num = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if bit & num:
                    nums.append(-1)  # 当前字符串里面有重复字符，直接设置为-1避免后续的组合使用
                    break
                else:
                    num |= bit
            else:
                nums.append(num)
        maxlen = 0

        # 回溯所有组合
        def backtrack(index, bits, prelen):
            nonlocal maxlen
            for i in range(index, n):
                if maxlens[i] + prelen < maxlen:  # 剪枝，如果剩下的字符最大长度+前面已组合的长度小于已计算的最大长度，退出
                    break
                if nums[i] > 0:  # 需要确保当前字符串本身没有重复字符
                    if nums[i] & bits == 0:  # 当前字符串与之前的组合没有重复字符，需要记录组合最长长度，然后进一步回溯
                        maxlen = max(maxlen, prelen + lens[i])
                        if index < n - 1:
                            backtrack(index + 1, nums[i] | bits, prelen + lens[i])

        backtrack(0, 0, 0)
        return maxlen


s = Solution()
print(s.maxLength(["a", "abc", "d", "de", "def"]))
print(s.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
print(s.maxLength(["un", "iq", "ue"]))
print(s.maxLength(["cha", "r", "act", "ers"]))
print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))

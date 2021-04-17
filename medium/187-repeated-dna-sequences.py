'''
重复的DNA序列
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，
识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
'''
from typing import List
'''
思路1，滑动窗口+位运算
将'A'，'C'，'G' , 'T' 映射为 0,1,2,3
长度为10的字符串可以压缩为位长为20的整数，滑动窗口遍历所有输入，每个位置的10位字符串都映射为整数，然后将其加入map中计数

时间复杂度：O(n)，遍历字符串一次
空间复杂度：O(n)，需要set保留所有的整数
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:  # 字符串<=10的情况下，不会有重复的序列
            return []
        mask = 0xfffff  # 20位的掩码
        intmap = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        strmap = ['A', 'C', 'G', 'T']
        nums = {}
        num = 0
        for i in range(10):  # 计算第1个整数
            num = (num << 2) | intmap[s[i]]
        nums[num] = 1
        for i in range(10, len(s)):  # 滑动窗口计算所有位置的整数
            num = ((num << 2) | intmap[s[i]]) & mask
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        ans = []
        li = [0] * 10
        for num, count in nums.items():
            if count > 1:
                for i in range(9, -1, -1):  # 使整数的高位先输出
                    li[i] = strmap[num & 3]
                    num >>= 2
                ans.append(''.join(li))
        return ans


s = Solution()
print(s.findRepeatedDnaSequences("GAGAGAGAGAGA"))
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(s.findRepeatedDnaSequences('AAAAAAAAAAAAA'))

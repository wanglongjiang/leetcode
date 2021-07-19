'''
面试题 01.04. 回文排列
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
'''
from collections import Counter
'''
思路：哈希计数
统计所有字母的个数，
如果要满足回文串，最多只有1个字符是奇数个，其他字符是偶数个

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd = 0
        for count in counter.values():
            if count % 2:
                odd += 1
                if odd > 1:
                    return False
        return True


s = Solution()
print(s.canPermutePalindrome("tactcoa"))

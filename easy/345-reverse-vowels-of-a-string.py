'''
反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
'''
'''
思路：哈希+双指针
将原因字母加入哈希表中
2个指针分布从2端向内搜索原因字母，如果遇到，进行交换
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        li = list(s)
        while left < right:
            while left < right and li[left] not in vowel:
                left += 1
            while left < right and li[right] not in vowel:
                right -= 1
            if left < right:
                li[left], li[right] = li[right], li[left]
                left += 1
                right -= 1
        return ''.join(li)


s = Solution()
print(s.reverseVowels("aA"))
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))

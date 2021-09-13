'''
反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
'''
from typing import List
'''
思路：双指针
2个指针从两端向中间移动，遍历数组并交换
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = Solution()
arr = ["h", "e", "l", "l", "o"]
print(s.reverseString(arr))
print(arr)
arr = ["H", "a", "n", "n", "a", "h"]
print(s.reverseString(arr))
print(arr)

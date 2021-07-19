'''
面试题 10.05. 稀疏数组搜索
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间
'''
from typing import List
import bisect
'''
思路：过滤后 二分查找
字符串过滤，只保留与s相同长度的，然后二分查找

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        m = len(s)
        indexs, words = zip(*filter(lambda w: len(w[1]) == m, enumerate(words)))
        index = bisect.bisect_left(words, s)
        if index == len(words):
            return -1
        if words[index] == s:
            return indexs[index]
        return -1


s = Solution()
print(s.findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ta"))
print(s.findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ball"))

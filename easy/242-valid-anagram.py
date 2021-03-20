'''
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
'''
'''
思路：设计一个长度26的数组counter，统计s内各个字母出现的频率，然后再遍历t内所有字符，出现的字符在counter内减掉
中间如果出现-1，不是字母异位词。
时间复杂度：O(s+t)
空间复杂度：O(1)
进阶，如果是unicode字符，可以用map实现

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for c in t:
            i = ord(c) - ord('a')
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True

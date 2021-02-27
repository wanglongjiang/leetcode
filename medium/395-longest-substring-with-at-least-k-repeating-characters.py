'''
至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
'''
'''
思路:回溯
首先遍历一遍字符串,统计里面每个字符出现的次数,
查找是否出现次数<k的字符c,
    如果没有,该字符串即为T,
    如果有,不满足要求,以其为边界切分出若干子字符串,对每个子字符串查找最长字串T,返回子字符串中的最大值
时间复杂度:O(n!)
空间复杂度:每个递归函数都辅助空间存储每个字符出现的次数,O(n!)
'''


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def backtrack(start: int, end: int):
            if end - start < k:  # 字符串长度小于k,肯定没有公共字串
                return 0
            counter = {}
            indexs = {}
            for i in range(start, end):
                if s[i] in counter:
                    counter[s[i]] += 1
                    indexs[s[i]].append(i)
                else:
                    counter[s[i]] = 1
                    indexs[s[i]] = [i]
            for key in counter:
                if counter[key] < k:
                    maxLen = 0
                    for index in indexs[key]:
                        maxLen = max(maxLen, backtrack(start, index))
                        start = index + 1
                    if end - start >= k:
                        maxLen = max(maxLen, backtrack(start, end))
                    return maxLen
            return end - start

        return backtrack(0, len(s))


s = Solution()
print(s.longestSubstring("bbaaacbd", 3))
print(s.longestSubstring("aaabb", 3))
print(s.longestSubstring("ababbc", 2))

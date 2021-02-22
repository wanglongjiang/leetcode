'''
字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
'''
from typing import List
'''
思路：每个单词按照字母顺序排序生成key加入词典，词典中每个key对应的value为列表。
空间复杂度：O(n)，最坏需要n个key空间
时间复杂度：O(n*logn) 针对每个单词都需要进行排序
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeKey(s: str):
            li = list(s)
            li.sort()
            return ''.join(li)

        groupDict = {}
        for s in strs:
            key = makeKey(s)
            if key not in groupDict:
                groupDict[key] = []
            groupDict[key].append(s)
        return list(groupDict.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

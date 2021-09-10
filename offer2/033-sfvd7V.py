'''
剑指 Offer II 033. 变位词组
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。

注意：若两个字符串中每个字符出现的次数都相同且字符顺序不完全相同，则称它们互为变位词。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
 

提示：

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
 

注意：本题与主站 49 题相同： https://leetcode-cn.com/problems/group-anagrams/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sfvd7V
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：哈希
每个单词按照字母顺序排序生成key加入词典，词典中每个key对应的value为列表。
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

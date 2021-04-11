'''
根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
'''
'''
思路：哈希表计数+排序
首先用哈希表对字符进行计数，然后对key,value进行排序
时间复杂度：O(n)
空间复杂度：O(charsetSize)
'''


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        charCnt = list(counter.items())
        charCnt.sort(key=lambda item: item[1], reverse=True)
        chars = []
        for item in charCnt:
            for i in range(item[1]):
                chars.append(item[0])
        return ''.join(chars)


s = Solution()
print(s.frequencySort("tree"))

'''
1772. 按受欢迎程度排列功能
给定一个字符串数组 features ，其中 features[i] 是一个单词，描述你最近参与开发的项目中一个功能的名称。你调查了用户喜欢哪些功能。
另给定一个字符串数组 responses，其中 responses[i] 是一个包含以空格分隔的一系列单词的字符串。

你想要按照受欢迎程度排列这些功能。 严格地说，令 appearances(word) 是满足 responses[i] 中包含单词 word 的 i 的个数，
则当 appearances(features[x]) > appearances(features[y]) 时，第 x 个功能比第 y 个功能更受欢迎。

返回一个数组 sortedFeatures ，包含按受欢迎程度排列的功能名称。当第 x  个功能和第 y 个功能的受欢迎程度相同且 x < y 时，你应当将第 x 个功能放在第 y 个功能之前。



示例 1：

输入：features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]
输出：["touch","cooler","lock"]
解释：appearances("cooler") = 1，appearances("lock") = 1，appearances("touch") = 2。由于 "cooler" 和 "lock" 都出现了 1 次，且 "cooler" 在原数组的前面，
所以 "cooler" 也应该在结果数组的前面。
示例 2：

输入：features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]
输出：["a","aa","b","c"]


提示：

1 <= features.length <= 10^4
1 <= features[i].length <= 10
features 不包含重复项。
features[i] 由小写字母构成。
1 <= responses.length <= 10^2
1 <= responses[i].length <= 10^3
responses[i] 由小写字母和空格组成。
responses[i] 不包含两个连续的空格。
responses[i] 没有前置或后置空格。
'''
from typing import List
'''
思路：哈希
将features加入哈希表
然后遍历responses，对于每个句子，需要拆分成单词，再将单词加入哈希表去重，去重后的单词在上面的哈希表中计数

时间复杂度：O(mn+lk)
空间复杂度：O(mn+lk)
'''


class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        allFeatures = {}
        for f in features:
            allFeatures[f] = 0
        for line in responses:
            for word in set(line.split(' ')):  # 句子拆分成单词，然后用集合去重
                if word in allFeatures:
                    allFeatures[word] += 1  # 计数+1
        return list(map(lambda p: p[1], sorted(map(lambda p: (-p[1], p[0]), allFeatures.items()))))  # 按照计数的从大到小，单词字典序排序


s = Solution()
print(s.sortFeatures(features=["cooler", "lock", "touch"], responses=["i like cooler cooler", "lock touch cool", "locker like touch"]))
print(s.sortFeatures(features=["a", "aa", "b", "c"], responses=["a", "a aa", "a a a a a", "b a"]))

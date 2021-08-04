'''
确定两个字符串是否接近
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

操作 1：交换任意两个 现有 字符。
例如，abcde -> aecdb
操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。

 

示例 1：

输入：word1 = "abc", word2 = "bca"
输出：true
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"
示例 2：

输入：word1 = "a", word2 = "aa"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
示例 3：

输入：word1 = "cabbba", word2 = "abbccc"
输出：true
解释：3 次操作从 word1 获得 word2 。
执行操作 1："cabbba" -> "caabbb"
执行操作 2："caabbb" -> "baaccc"
执行操作 2："baaccc" -> "abbccc"
示例 4：

输入：word1 = "cabbba", word2 = "aabbss"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
 

提示：

1 <= word1.length, word2.length <= 10^5
word1 和 word2 仅包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/determine-if-two-strings-are-close
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import Counter
'''
思路：哈希
题目中允许任意交换2个字符的位置，允许任意交换2个字符的种类，那么也就是说
只要字符串中各个字符的个数组合相同就是接近的。
可以用哈希表分别统计2个字符串的字符个数，然后对比字符的个数集合是否相同

TODO

时间复杂度：O(nlogn)，计数需要O(n)，字符的个数需要进行排序
空间复杂度：O(n)
'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1, count2 = Counter(word1), Counter(word2)
        for c1, c2 in zip(count1.most_common(), count2.most_common()):
            if c1[1] != c2[1]:
                return False
        return True


s = Solution()
print(s.closeStrings(word1="abc", word2="bca"))
print(s.closeStrings(word1="a", word2="aa"))
print(s.closeStrings(word1="cabbba", word2="abbccc"))
print(s.closeStrings(word1="cabbba", word2="aabbss"))

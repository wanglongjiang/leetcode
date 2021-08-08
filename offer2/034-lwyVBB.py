'''
剑指 Offer II 034. 外星语言是否排序
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

 

示例 1：

输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
示例 2：

输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
示例 3：

输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。
 

注意：本题与主站 953 题相同： https://leetcode-cn.com/problems/verifying-an-alien-dictionary/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lwyVBB
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：哈希 数组
1. 将字母和其索引加入哈希表
2. 依次对比每个words[i],words[i+1]，使得每个字符按照哈希表中的顺序升序

时间复杂度：O(mn),m=len(words),n=len(words[i])
空间复杂度：O(1)
'''


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charOrder = {}
        for i, char in enumerate(order):
            charOrder[char] = i
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i]) and j < len(words[i - 1]):
                if charOrder[words[i][j]] == charOrder[words[i - 1][j]]:
                    j += 1
                elif charOrder[words[i][j]] < charOrder[words[i - 1][j]]:
                    return False
                else:
                    break
            else:
                if j < len(words[i - 1]):  # 如果前一个单词未对比完成，说明前一个单词不小于等于后一个单词，需要返回false
                    return False
        return True

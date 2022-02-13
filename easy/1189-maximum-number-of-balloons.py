'''
1189. “气球” 的最大数量
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

 

示例 1：



输入：text = "nlaebolko"
输出：1
示例 2：



输入：text = "loonbalxballpoon"
输出：2
示例 3：

输入：text = "leetcode"
输出：0
 

提示：

1 <= text.length <= 10^4
text 全部由小写英文字母组成
'''
from typing import Counter
'''
思路：计数
用哈希表对所有字符个数进行计数，然后查看balon5个字符的个数

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count['a'], count['b'], count['l'] // 2, count['o'] // 2, count['n'])

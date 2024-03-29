'''
查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]
 

提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from functools import reduce
from collections import Counter
'''
思路：计数
对每个单词中的字符进行计数，然后求其交集

时间复杂度：O(mn),m=len(words),n=len(words[i])
空间复杂度：O(mn)
'''


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(lambda word: Counter(word), words)).elements())

'''
划分字母区间

字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
201
S只包含小写字母 'a' 到 'z' 。
'''
from typing import List
from collections import Counter
'''
思路：贪心+哈希计数
1. 先对字符串所有字符计数
2. 设置2个集合subSet和remainderSet，subSet用于保存当前已遍历子串的字符集合，remainderSet用于保存剩余未遍历子串的字符集合
3. 遍历字符串，已遍历过的字符从计数器中删除，如果字符计数为0，从remainderSet中删除，此时检查subSet与remainderSet是否有交集
如果没有交集，此时的字符串为成功的划片，left指针指向下一个位置；否则继续遍历。

时间复杂度：O(n^2)，对于每个要删除的字符，都要判断是否有交集，因此时间复杂度为O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        subSet, remainder = set(), set(s)
        left, right = 0, 0
        n = len(s)
        ans = []
        while right < n:
            subSet.add(s[right])  # 将该字符添加到已遍历集合里
            counter[s[right]] -= 1
            if counter[s[right]] == 0:  # 一个字符已经在后面没有了
                remainder.remove(s[right])  # 将改字符从集合中删除
                if subSet.isdisjoint(remainder):  # 没有交集，是成功的切片
                    ans.append(right - left + 1)
                    left = right + 1
            right += 1
        if right > left:
            ans.append(right - left)
        return ans


s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))

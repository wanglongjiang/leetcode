'''
火星词典

现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 

示例 1：

输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
示例 2：

输入：words = ["z","x"]
输出："zx"
示例 3：

输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/Jf1JuT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
from collections import deque
'''
思路：拓扑排序
1. 两两对比words中的字符串，
设单词words[i]、words[j]中第1个不同的字符为charA,charB，就有charA→charB的一条边。
该过程创建了有向图graph，图中的节点为英文字符，边为前后顺序
2. 拓扑排序graph，
如果图中有环，则不存在合法的字母顺序，返回''
如果图中没有环，返回字母的拓扑排序

时间复杂度：O(mn)，m=words.length,n=words[i].length
空间复杂度：O(26n)
'''


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        m = len(words)
        graph = defaultdict(list)  # 有向图
        indegree = defaultdict(int)  # 保存各个节点的入度
        allChars = set()  # 保存所有的字母
        for word in words:
            allChars.update(word)
        for i in range(1, m):
            word1, word2 = words[i - 1], words[i]
            j, k = 0, 0
            while j < len(word1) and k < len(word2) and word1[j] == word2[k]:
                j += 1
                k += 1
            if j < len(word1) and k < len(word2):
                graph[word1[j]].append(word2[k])
                indegree[word2[k]] += 1
            elif j < len(word1) and k == len(word2):  # 特殊情况，如果word2是word1的子串，不满足题意
                return ''
        # 进行拓扑排序
        ans = []
        q = deque()
        for char in allChars:
            if char not in indegree:
                q.append(char)
        while q:
            char = q.popleft()
            ans.append(char)
            for nextchar in graph[char]:
                indegree[nextchar] -= 1
                if indegree[nextchar] == 0:
                    q.append(nextchar)
        if len(ans) == len(allChars):  # 没有环路，所有的字符都会被输出
            return ''.join(ans)
        return ''  # 存在环路

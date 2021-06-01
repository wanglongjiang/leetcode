'''
驼峰式匹配
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

 

示例 1：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".

示例 2：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".

示例 3：

输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释：
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
 

提示：

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
所有字符串都仅由大写和小写英文字母组成。
'''
from typing import List
'''
思路：字符串对比
依次对比pattern与每个单词queries[i]，对比方法为：
1. 如果pattern[i] == query[i]则继续比较下一个字符
2. 如果pattern[i] != query[i]且query[i]是小写字母，跳过query[i]，比较query[i+1]，直至两个字符相同；如果query[j]为大写字母或者到了末尾，则返回False
3. 重复上面过程，直至pattern所有字符都被对比成功。

时间复杂度：O(mnl),m为pattern长度，n为queries[i].length,l为queries.length
空间复杂度：O(1)，除了返回数组，没有多余的空间
'''


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m = len(pattern)
        ans = []
        for query in queries:
            j, n = 0, len(query)
            for i in range(m):
                while j < n and pattern[i] != query[j] and query[j].islower():
                    j += 1
                if j == n or pattern[i] != query[j]:
                    ans.append(False)
                    break
                i += 1
                j += 1
            else:
                while j < n and query[j].islower():  # 遍历query剩下的字符，如果还有大写字母，返回False
                    j += 1
                if j == n:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans


s = Solution()
print(s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
print(s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa"))
print(s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBaT"))

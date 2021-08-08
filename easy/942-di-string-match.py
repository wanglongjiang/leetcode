'''
增减字符串匹配
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
 

示例 1：

输入："IDID"
输出：[0,4,1,3,2]
示例 2：

输入："III"
输出：[0,1,2,3]
示例 3：

输入："DDI"
输出：[3,2,0,1]
 

提示：

1 <= S.length <= 10000
S 只包含字符 "I" 或 "D"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-string-match
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：双指针 贪心
根据题意，如果遇到D，需要数字减小，如果遇到I，需要数字增大。
可以设置left，right指针，初始分别指向0和len(s)，在下面的遍历过程中，rihgt永远>=left
遍历s：
> 当遇到D，right进入结果list，同时right-1。后面如果是D，那么下一个是right-1进入list，成立；后面如果是I，因为right>left，也成立。
> 当遇到I，left进入结果list，同时left+1。后面如果是D，那么下一个是right进入list，因为right>left成立；后面如果是I，因为left<left+1，也成立。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        ans = []
        for c in s:
            if c == 'D':
                ans.append(right)
                right -= 1
            else:
                ans.append(left)
                left += 1
        ans.append(right)
        return ans

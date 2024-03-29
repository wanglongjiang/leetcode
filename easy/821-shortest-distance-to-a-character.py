'''
字符的最短距离
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

 

示例 1：

输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 3 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
示例 2：

输入：s = "aaab", c = "b"
输出：[3,2,1,0]
 

提示：
1 <= s.length <= 10^4
s[i] 和 c 均为小写英文字母
题目数据保证 c 在 s 中至少出现一次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：数组
设数组ans,长度为n=len(s)，初始值均为n
然后遍历s，对于当前字符s[i]
> 如果s[i]==c，则ans[i]=0，
>> 向左遍历ans，初始设j=i-1，ans[j]=ans[j+1]-1，直至原ans[j]不再小于新的值或者遇到s的开头
>> 向右遍历ans, 初始设j=i+1, ans[j]=ans[j-1]+1,直至s[i]==c或者遇到末尾

时间复杂度：O(n)，ans每个元素最多被赋值2次（算上初始化，最多3次），因此时间复杂度是O(n)
空间复杂度：O(1)
'''


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        for i in range(n):
            if s[i] == c:
                ans[i] = 0
                for j in range(i - 1, -1, -1):  # 向左尝试修改与c的距离
                    if ans[j] <= ans[j + 1]:
                        break
                    ans[j] = ans[j + 1] + 1
                for j in range(i + 1, n):  # 向右尝试修改与c的距离
                    if s[j] == c:
                        break
                    ans[j] = ans[j - 1] + 1
        return ans

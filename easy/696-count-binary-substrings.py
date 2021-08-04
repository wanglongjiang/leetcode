'''
计数二进制子串
给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

 

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
 

提示：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：滑动窗口
设left,mid,right3个指针，left指向连续的01子串开始，mid指向0,1分解，right指向连续的01子串末尾
初始left指向0
1. 向右移动right指针，直至s[left]!=s[right]，此时mid=left
2. 向右继续移动right指针，直至s[left]==s[right]，此时left和right内部是一个连续的01子串，这个子串内的连续子串的数量是min(mid-left,right-mid)
3. 向右移动left，使left=mid
持续以上过程，直至right指针指向s的末尾

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        left, mid, right = 0, 0, 0
        ans = 0
        while right < n:
            while right < n and s[left] == s[right]:  # 向右移动right指针，直至s[left]!=s[right]
                right += 1
            mid = right
            while right < n and s[left] != s[right]:  # 向右继续移动right指针，直至s[left]==s[right]
                right += 1
            ans += min(mid - left, right - mid)
            left = mid
        return ans

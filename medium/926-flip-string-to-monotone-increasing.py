'''
将字符串翻转到单调递增

如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是 单调递增 的。

我们给出一个由字符 '0' 和 '1' 组成的字符串 s，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。

返回使 s 单调递增 的最小翻转次数。

 

示例 1：

输入：s = "00110"
输出：1
解释：我们翻转最后一位得到 00111.
示例 2：

输入：s = "010110"
输出：2
解释：我们翻转得到 011111，或者是 000111。
示例 3：

输入：s = "00011000"
输出：2
解释：我们翻转得到 00000000。
 

提示：

1 <= s.length <= 20000
s 中只包含字符 '0' 和 '1'
 

注意：本题与主站 926 题相同： https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cyJERH
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：贪心
从左向右遍历字符串，遇到第1个'1'之后，
> 如果当前字符是1，将1的计数oneCount+1
> 如果当前字符是0，将0的计数zeroCount+1，
>> 如果zeroCount=oneCount，此时至少需要变动zeroCount个0或者oneCount个1，因此将变动次数ans+1,将zeroCount和oneCount清零
>> 如果zeroCount>oneCount=0,此时的0可以忽略，将zeroCount清零
>> 如果0=zeroCount<oneCount，无法确定是翻转0还是翻转1，跳过

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one, zero, ans = 0, 0, 0
        for c in s:
            if c == '1':
                one += 1
            elif c == '0':
                zero += 1
                if one == zero:  # 1和后面出现的0个数相同，此时至少需要翻转其中一半的数字
                    ans += one
                    zero = 0
                    one = 0
                elif zero > 0 and one == 0:  # 前导0，或者前面的0，1翻转后新出现的0可以忽略
                    zero = 0
        if one > zero > 0:
            ans += zero
        return ans

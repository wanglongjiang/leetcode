'''
2266. 统计打字方案数
Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。



为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。

比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。

比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。

由于答案可能很大，将它对 109 + 7 取余 后返回。

 

示例 1：

输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
示例 2：

输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 109 + 7 取余，所以我们返回 2082876103 % (109 + 7) = 82876089 。
 

提示：

1 <= pressedKeys.length <= 105
pressedKeys 只包含数字 '2' 到 '9' 。
'''
'''
思路：动态规划
连续相同的数字构成的一个子串，根据该数字能够映射成的字母可以任意组合。
组合的数量与子串长度和该数字映射的字母数量有关，计算这个可以用动态规划。
dp[i]意思是子串中截止第i个字符的组合数，
dp[0] =1
当数字能映射3个字母时：
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]，意思是当前数字映射成第1个字符的方案数+映射成第2个字符的方案数+映射成第3个字符的方案数
当数字能映射4个字母时：
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]，与上面意思类同

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        numMap = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}

        # 该函数用动态规划计算一个子串的可能组合数
        def calc(sublen, count):
            dp = [0] * sublen
            dp[0] = 1
            for i in range(1, sublen):
                dp[i] = dp[i - 1]
                if i > 0:
                    dp[i] += dp[i - 2] if i > 1 else 1
                if i > 1:
                    dp[i] += dp[i - 3] if i > 2 else 1
                if count > 3 and i > 2:
                    dp[i] += dp[i - 4] if i > 3 else 1
            return dp[-1] % m

        char, sublen = pressedKeys[0], 1
        ans, m = 0, 10**9 + 7
        for ch in pressedKeys[1:]:
            if char != ch:
                ans = (ans * calc(sublen, numMap[char])) % m if ans > 0 else calc(sublen, numMap[char]) % m
                char = ch
                sublen = 1
            else:
                sublen += 1
        ans = (ans * calc(sublen, numMap[char])) % m if ans > 0 else calc(sublen, numMap[char]) % m
        return ans


s = Solution()
print(s.countTexts("222"))
print(s.countTexts("2222"))
print(s.countTexts("22233"))
print(s.countTexts("222222222222222222222222222222222222"))

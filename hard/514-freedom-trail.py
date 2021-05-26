'''
自由之路

电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

旋转 ring 拼出 key 字符 key[i] 的阶段中：

您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
示例：
输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。

提示：

ring 和 key 的字符串长度取值范围均为 1 至 100；
两个字符串中都只有小写字符，并且均可能存在重复字符；
字符串 key 一定可以由字符串 ring 旋转拼出。
'''
'''
思路：动态规划
对于key中的任意字符key[i]，ring中可能有3个索引可以满足key[i]==ring[a] or ring[b] or ring[c]，对于key[i+1]，ring中可能有2个索引可以满足key[i+1]==ring[e] or ring[f]
那么，从key[i]到key[i+1]，如果key[i+1]匹配到ring[e]，那么在key[i+1]+ring[e]这个组合下移动的单次最小距离是min(e-a,e-b,e-c)，假设我们之前已经计算出在key[i]时的最小移动距离
dp[i][a],dp[i][b],dp[i][c]，那么在dp[i+1][e]点的最小移动距离就是min(dp[i][a]+abs(e-a),dp[i][b]+abs(e-b),dp[i][c]+abs(e-c))+1。
同理如果key[i+1]匹配到ring[f]，按照上面e点的方法可以计算出key[i+1]+ring[f]的最小移动距离。
根据上面的思路，设一个动态规划数组dp，对于dp[i][j]代表的含义是key的第i个字符与ring第j个字符匹配时，最小移动距离
dp[i][j] = min(dp[i-1][a]+abs(j-a), dp[i-1][b]+abs(j-b)...)+1 且满足key[i]==ring[j],dp[i-1][a...b]>0
dp[i][j] = 最大整数，此时key[i]!=ring[j]

注：上面的状态转移方程里面计算移动距离abs(j-a)，没有考虑ring可以旋转一周，如果可以360度旋转，需要修改

时间复杂度：O(n*m^2)，n为key.length,m为ring.length
空间复杂度：O(n*m)
'''


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(key), len(ring)
        dp = [[float('inf')] * m for _ in range(n)]
        for j in range(m):  # 设置第0个字符匹配的距离
            if key[0] == ring[j]:
                dp[0][j] = j + 1  # ring一开始第0个字符处于激活状态，其他位置的字符都需要旋转j步
        for i in range(1, n):
            for j in range(m):
                if key[i] == ring[j]:
                    for k in range(m):
                        if dp[i - 1][k] > 0:
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + 1 + abs(j - k))
        return min(dp[n - 1])


s = Solution()
print(s.findRotateSteps(ring="godding", key="gd"))

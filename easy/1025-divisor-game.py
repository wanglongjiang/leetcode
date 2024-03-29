'''
除数博弈
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
 

提示：

1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divisor-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学 博弈
观察得到N=1，输；N=2，赢；N=3，输。。。
假设N=奇数会输，N=偶数会赢，
当N=奇数时，如果想要赢，让N-x仍然是奇数，x必须是偶数，但N为奇数的情况下N%x不可能为0，故N为奇数必输
当N=偶数时，x选择1，N%X为0，满足要求，N-x为奇数，会造成对方必输

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

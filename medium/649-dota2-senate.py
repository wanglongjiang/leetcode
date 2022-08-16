'''
649. Dota2 参议院
Dota2 的世界里有两个阵营：Radiant(天辉)和 Dire(夜魇)

Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。
在每一轮中，每一位参议员都可以行使两项权利中的一项：

禁止一名参议员的权利：

参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。

宣布胜利：

如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。



给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。
然后，如果有 n 个参议员，给定字符串的大小将是 n。

以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。

假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。
输出应该是 Radiant 或 Dire。



示例 1：

输入："RD"
输出："Radiant"
解释：第一个参议员来自 Radiant 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。
然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人
示例 2：

输入："RDD"
输出："Dire"
解释：
第一轮中,第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
第二个来自 Dire 阵营的参议员会被跳过因为他的权利被禁止
第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利


提示：

给定字符串的长度在 [1, 10,000] 之间.
'''
'''
思路：贪心 模拟 双指针
模拟议员的操作，具体算法是：
设置2个指针aliveR,aliveD指向存活的2个阵营的议员，初始都指向第1个己方的议员。
遍历senate，对于当前议员i
* 如果i<己方alive指针，i已经被禁止掉，需要跳过。
* 如果不满足上述条件，移动对方阵营的alive指针，向后找第1个对方阵营的人，如果找到，将alive指针指向找到的索引后面，如果找不到，说明己方阵营获胜。
重复上述过程，直至2个指针之一超出n，也就是没有存活的议员。

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        alive = {'R': float('inf'), 'D': float('inf')}  # 目前存活的议员指针，指针左侧的议员是被投票封杀的，指针右侧的是存活的
        for i in range(n):  # 查找第1位议员
            alive[senate[i]] = min(alive[senate[i]], i)
            if alive['R'] < n and alive['D'] < n:
                break
        if alive['R'] == float('inf'):
            return 'Dire'
        if alive['D'] == float('inf'):
            return 'Radiant'
        while alive['R'] < n and alive['D'] < n:  # 进行多轮投票，直至某一方不再有存活的议员
            for i in range(min(alive['R'], alive['D']), n):  # 从较小的索引，也就是优先投票的阵营开始遍历
                s = senate[i]  # s为当前阵营的简称
                o = 'R' if s == 'D' else 'D'  # 取得对方阵营的简称
                if i >= alive[s]:  # i>alive，属于存活的议员，有投票权，需要执行下面的操作
                    alive[o] += 1  # 对方阵营的一个议员被禁掉
                    while alive[o] < n and senate[alive[o]] == s:  # 移动对方阵营指针，指到下一个议员
                        alive[o] += 1
        return 'Dire' if alive['R'] == n else 'Radiant'  # 还有剩余议员的阵营获胜


s = Solution()
print(s.predictPartyVictory("DRD" == "Dire"))  # TODO
print(s.predictPartyVictory("DDD") == "Dire")
print(s.predictPartyVictory("RDRDDD"))
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
print(s.predictPartyVictory("RDRDD"))

'''
通过投票对团队排名
现在有一个特殊的排名系统，依据参赛团队在投票人心中的次序进行排名，每个投票者都需要按从高到低的顺序对参与排名的所有团队进行排位。

排名规则如下：

参赛团队的排名次序依照其所获「排位第一」的票的多少决定。如果存在多个团队并列的情况，将继续考虑其「排位第二」的票的数量。
以此类推，直到不再存在并列的情况。
如果在考虑完所有投票情况后仍然出现并列现象，则根据团队字母的字母顺序进行排名。
给你一个字符串数组 votes 代表全体投票者给出的排位情况，请你根据上述排名规则对所有参赛团队进行排名。

请你返回能表示按排名系统 排序后 的所有团队排名的字符串。

 

示例 1：
输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
输出："ACB"
解释：A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
B 队获得两票「排位第二」，三票「排位第三」。
C 队获得三票「排位第二」，两票「排位第三」。
由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。

示例 2：
输入：votes = ["WXYZ","XYZW"]
输出："XWYZ"
解释：X 队在并列僵局打破后成为排名第一的团队。X 队和 W 队的「排位第一」票数一样，但是 X 队有一票「排位第二」，
而 W 没有获得「排位第二」。

示例 3：
输入：votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
输出："ZMNAGUEDSJYLBOPHRQICWFXTVK"
解释：只有一个投票者，所以排名完全按照他的意愿。

示例 4：
输入：votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
输出："ABC"
解释：
A 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
B 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
C 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
完全并列，所以我们需要按照字母升序排名。

示例 5：
输入：votes = ["M","M","M","M"]
输出："M"
解释：只有 M 队参赛，所以它排名第一。
'''
from typing import List
'''
思路：排序
1、设n=votes[0].length，设一个n*n的二维数组，先对各队的名次进行计数
2、对二维数组从后向前进行n次排序（基数排序，因n最大是26，单次排序可以用冒泡排序）

时间复杂度：O(m+n^3)，m为votes.length,n为votes[i].length
空间复杂度：O(n^2)
'''


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        nameToIdx, idxToName = {}, {}
        names = list(votes[0])
        names.sort()  # 队名按照字母顺序
        for i in range(n):
            nameToIdx[names[i]] = i
            idxToName[i] = names[i]
        counter = [[0] * n for _ in range(n)]  # 第1维存放的是队索引，第2列存放的是各个名次的得票数
        for v in votes:
            for i in range(n):
                counter[nameToIdx[v[i]]][i] += 1
        for i in range(n - 1, -1, -1):  # 名次从后往前基数排序
            for j in range(1, n):  # 冒泡排序第i个名次的数据
                for k in range(j, 0, -1):
                    if counter[k][i] > counter[k - 1][i]:
                        counter[k], counter[k - 1] = counter[k - 1], counter[k]
                        idxToName[k], idxToName[k - 1] = idxToName[k - 1], idxToName[k]
        ans = []
        for i in range(n):
            ans.append(idxToName[i])
        return ''.join(ans)


s = Solution()
print(s.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]) == 'ABC')
print(s.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]) == "ACB")
print(s.rankTeams(["WXYZ", "XYZW"]) == 'XWYZ')
print(s.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]) == 'ZMNAGUEDSJYLBOPHRQICWFXTVK')
print(s.rankTeams(["M", "M", "M", "M"]) == 'M')

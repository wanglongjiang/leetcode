'''

作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」
（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。

所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，
团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：

例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。

提示：

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] 由小写英文字母组成
req_skills 中的所有字符串 互不相同
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] 由小写英文字母组成
people[i] 中的所有字符串 互不相同
people[i] 中的每个技能是 req_skills 中的技能
题目数据保证「必要团队」一定存在
'''
from typing import List
'''
思路1，位运算+回溯。
1、因为最多有16个技能，可以将项目的每个技能用1bit来表示，整个项目的技能需求可以用1个整数表示。
2、计算每个人掌握的技能集合，压缩成1个整数
3、回溯从每个人出发，查找技能组合与目标相同的人的组合
'''


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 计算整数中1的个数的汉明函数
        def hammingWeight(n: int) -> int:
            cnt = 0
            while n > 0:
                n &= (n - 1)
                cnt += 1
            return cnt

        # 1、计算出所有的技能索引
        m, n = len(people), len(req_skills)
        allSkills = 0
        skillIndex = {}
        for i in range(n):
            allSkills = allSkills << 1 | 1
            skillIndex[req_skills[i]] = i
        # 2、计算每个人掌握的技能集合，压缩成1个整数
        peopleSkills = [0] * m
        peopleSkillNums = []
        for i in range(m):
            skillNums = len(people[i])
            if skillNums == n:  # 1个人掌握所有技能，直接返回
                return [i]
            if skillNums == 0:
                continue
            peopleSkillNums.append((i, skillNums))  # 计算每个人掌握的技能数
            for skill in people[i]:
                peopleSkills[i] |= 1 << skillIndex[skill]
        # 将技能被其他人包含的人筛选掉
        m = len(peopleSkillNums)
        for i in range(m - 1):
            for j in range(i + 1, m):
                if peopleSkillNums[i] and peopleSkillNums[j]:
                    p1Skill = peopleSkills[peopleSkillNums[i][0]]
                    p2Skill = peopleSkills[peopleSkillNums[j][0]]
                    intersection = p1Skill & p2Skill
                    if p1Skill == intersection:
                        peopleSkillNums[i] = None
                        break
                    if p2Skill == intersection:
                        peopleSkillNums[j] = None
        peopleSkillNums = list(filter(lambda x: x is not None, peopleSkillNums))
        peopleSkillNums.sort(key=lambda x: x[1], reverse=True)  # 根据技能数量倒序排序
        m = len(peopleSkillNums)
        remainderSkillNums = [0] * m
        remainderSkills = [0] * m
        skill = 0
        for i in range(m - 1, -1, -1):
            skill |= peopleSkills[peopleSkillNums[i][0]]
            remainderSkills[i] = skill
            remainderSkillNums[i] = hammingWeight(skill)

        # 3、回溯从每个人出发，查找技能组合与目标相同的人的组合

        ans = []
        candidate = []
        minPeople = m + 1

        def backtrack(index, pepoleNum, targetSkill):
            nonlocal minPeople, ans
            if remainderSkills[index] & targetSkill != targetSkill:  # 剪枝，如果剩余的技能不能包含需求技能时，直接退出
                return
            needSkillCnt = hammingWeight(targetSkill)
            for i in range(index, m):
                peopleIndex, skillNum = peopleSkillNums[i]
                if remainderSkillNums[i] < needSkillCnt:  # 剪枝，剩余人掌握的技能数肯定无法满足时，直接退出
                    return
                newTargetSkill = ~peopleSkills[peopleIndex] & targetSkill
                if newTargetSkill == targetSkill:  # 剪枝，没有贡献新技能，跳过
                    continue
                candidate.append(peopleIndex)
                if newTargetSkill == 0:
                    if minPeople > pepoleNum + 1:
                        minPeople = pepoleNum + 1
                        ans = candidate.copy()
                    candidate.pop()
                    return  # 剪枝，如果该层已经找到一个解，不需要继续了
                else:
                    if minPeople > pepoleNum + 1:  # 剪枝，如果最少人数少于当前人数，不需要回溯了
                        backtrack(index + 1, pepoleNum + 1, newTargetSkill)
                candidate.pop()

        backtrack(0, 0, allSkills)
        return ans


s = Solution()
print(
    s.smallestSufficientTeam([
        "hfkbcrslcdjq", "jmhobexvmmlyyzk", "fjubadocdwaygs", "peaqbonzgl", "brgjopmm", "x", "mf", "pcfpppaxsxtpixd", "ccwfthnjt", "xtadkauiqwravo", "zezdb",
        "a", "rahimgtlopffbwdg", "ulqocaijhezwfr", "zshbwqdhx", "hyxnrujrqykzhizm"
    ], [["peaqbonzgl", "xtadkauiqwravo"], ["peaqbonzgl", "pcfpppaxsxtpixd", "zshbwqdhx"], ["x", "a"], ["a"],
        ["jmhobexvmmlyyzk", "fjubadocdwaygs", "xtadkauiqwravo", "zshbwqdhx"], ["fjubadocdwaygs", "x", "zshbwqdhx"], ["x", "xtadkauiqwravo"],
        ["x", "hyxnrujrqykzhizm"], ["peaqbonzgl", "x", "pcfpppaxsxtpixd", "a"], ["peaqbonzgl", "pcfpppaxsxtpixd"], ["a"], ["hyxnrujrqykzhizm"],
        ["jmhobexvmmlyyzk"], ["hfkbcrslcdjq", "xtadkauiqwravo", "a", "zshbwqdhx"], ["peaqbonzgl", "mf", "a", "rahimgtlopffbwdg", "zshbwqdhx"], [
            "xtadkauiqwravo"
        ], ["fjubadocdwaygs"], ["x", "a", "ulqocaijhezwfr", "zshbwqdhx"], ["peaqbonzgl"], ["pcfpppaxsxtpixd", "ulqocaijhezwfr", "hyxnrujrqykzhizm"],
        ["a", "ulqocaijhezwfr", "hyxnrujrqykzhizm"], ["a", "rahimgtlopffbwdg"], ["zshbwqdhx"], ["fjubadocdwaygs", "peaqbonzgl", "brgjopmm", "x"],
        ["hyxnrujrqykzhizm"], ["jmhobexvmmlyyzk", "a", "ulqocaijhezwfr"], ["peaqbonzgl", "x", "a", "ulqocaijhezwfr", "zshbwqdhx"], ["mf", "pcfpppaxsxtpixd"],
        ["fjubadocdwaygs", "ulqocaijhezwfr"], ["fjubadocdwaygs", "x", "a"], ["zezdb", "hyxnrujrqykzhizm"], ["ccwfthnjt", "a"], ["fjubadocdwaygs", "zezdb", "a"],
        [], ["peaqbonzgl", "ccwfthnjt", "hyxnrujrqykzhizm"], ["xtadkauiqwravo", "hyxnrujrqykzhizm"], ["peaqbonzgl", "a"], ["x", "a", "hyxnrujrqykzhizm"],
        ["zshbwqdhx"], [], ["fjubadocdwaygs", "mf", "pcfpppaxsxtpixd", "zshbwqdhx"], ["pcfpppaxsxtpixd", "a", "zshbwqdhx"], ["peaqbonzgl"],
        ["peaqbonzgl", "x", "ulqocaijhezwfr"], ["ulqocaijhezwfr"], ["x"], ["fjubadocdwaygs", "peaqbonzgl"], ["fjubadocdwaygs", "xtadkauiqwravo"],
        ["pcfpppaxsxtpixd", "zshbwqdhx"], ["peaqbonzgl", "brgjopmm", "pcfpppaxsxtpixd", "a"], ["fjubadocdwaygs", "x", "mf", "ulqocaijhezwfr"],
        ["jmhobexvmmlyyzk", "brgjopmm", "rahimgtlopffbwdg", "hyxnrujrqykzhizm"], ["x", "ccwfthnjt", "hyxnrujrqykzhizm"], ["hyxnrujrqykzhizm"],
        ["peaqbonzgl", "x", "xtadkauiqwravo", "ulqocaijhezwfr", "hyxnrujrqykzhizm"], ["brgjopmm", "ulqocaijhezwfr", "zshbwqdhx"],
        ["peaqbonzgl", "pcfpppaxsxtpixd"], ["fjubadocdwaygs", "x", "a", "zshbwqdhx"], ["fjubadocdwaygs", "peaqbonzgl", "x"], ["ccwfthnjt"]]))

print(
    s.smallestSufficientTeam(
        ["hkyodbbhr", "p", "biflxurxdvb", "x", "qq", "yhiwcn"],
        [["yhiwcn"], [], [], [], ["biflxurxdvb", "yhiwcn"], ["hkyodbbhr"], ["hkyodbbhr", "p"], ["hkyodbbhr"], [], ["yhiwcn"], ["hkyodbbhr", "qq"], ["qq"],
         ["hkyodbbhr"], ["yhiwcn"], [], ["biflxurxdvb"], [], ["hkyodbbhr"], ["hkyodbbhr", "yhiwcn"], ["yhiwcn"], ["hkyodbbhr"], ["hkyodbbhr", "p"], [], [],
         ["hkyodbbhr"], ["biflxurxdvb"], ["qq", "yhiwcn"], ["hkyodbbhr", "yhiwcn"], ["hkyodbbhr"], [], [], ["hkyodbbhr"], [], ["yhiwcn"], [], ["hkyodbbhr"],
         ["yhiwcn"], ["yhiwcn"], [], [], ["hkyodbbhr", "yhiwcn"], ["yhiwcn"], ["yhiwcn"], [], [], [], ["yhiwcn"], [], ["yhiwcn"], ["x"], ["hkyodbbhr"], [], [],
         ["yhiwcn"], [], ["biflxurxdvb"], [], [], ["hkyodbbhr", "biflxurxdvb", "yhiwcn"], []]))
print(
    s.smallestSufficientTeam(
        ["hxlk", "wgqsztvrgjbkxw", "ucrkmmkekmuks", "gjpqressg", "xbnmjd", "odwwreaiwdsbm", "kmystbjncopsf", "fsl", "wbdvwwdl"],
        [["gjpqressg", "xbnmjd"], ["fsl"], ["ucrkmmkekmuks", "odwwreaiwdsbm"], ["hxlk"], [], ["hxlk", "wbdvwwdl"], ["ucrkmmkekmuks", "fsl", "wbdvwwdl"],
         ["kmystbjncopsf"], ["ucrkmmkekmuks", "fsl"], ["gjpqressg"], [], ["xbnmjd", "odwwreaiwdsbm", "fsl"], ["fsl"], ["ucrkmmkekmuks", "gjpqressg", "fsl"],
         ["gjpqressg", "fsl"], ["ucrkmmkekmuks", "gjpqressg"], ["wbdvwwdl"], [], ["hxlk", "ucrkmmkekmuks", "gjpqressg", "fsl"], ["fsl"], ["hxlk", "fsl"],
         ["ucrkmmkekmuks"], ["hxlk"], ["gjpqressg"], ["ucrkmmkekmuks"], [], ["wgqsztvrgjbkxw", "fsl", "wbdvwwdl"], ["ucrkmmkekmuks"], ["gjpqressg"], ["xbnmjd"],
         ["hxlk", "gjpqressg", "fsl"], ["kmystbjncopsf", "fsl"], ["gjpqressg", "fsl"], [], ["fsl", "wbdvwwdl"], ["hxlk"], ["fsl", "wbdvwwdl"],
         ["ucrkmmkekmuks", "gjpqressg"], ["fsl"], ["ucrkmmkekmuks", "gjpqressg"], ["kmystbjncopsf"], ["hxlk"], ["hxlk"], ["hxlk", "gjpqressg"],
         ["hxlk", "fsl", "wbdvwwdl"], ["gjpqressg", "wbdvwwdl"], [], [], [], [], [], ["wgqsztvrgjbkxw", "gjpqressg", "wbdvwwdl"], ["hxlk", "xbnmjd"],
         ["gjpqressg", "fsl"], ["kmystbjncopsf"], ["gjpqressg", "fsl"], ["gjpqressg"], [], [], ["xbnmjd"]]))
print(s.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"], people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
print(
    s.smallestSufficientTeam(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                             people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"], ["reactjs", "csharp"],
                                     ["csharp", "math"], ["aws", "java"]]))

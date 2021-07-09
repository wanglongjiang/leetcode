'''
收藏清单
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。

请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

 

示例 1：

输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4]
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=
["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
示例 2：

输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1]
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
示例 3：

输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]
 

提示：

1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
favoriteCompanies[i] 中的所有字符串 各不相同 。
用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。
所有字符串仅包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：哈希
首先遍历依次所有清单，将公司名映射为编号。
然后用2重循环对比2个用户的清单是否为子集关系，将是子集的用户编号加入哈希表subset。
最后将不在subset中的编号输出到list

时间复杂度：O(n^2*m),n=favoriteCompanies.length,m=favoriteCompanies[i].length
空间复杂度：O(n*m)
'''


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        companyMap = {}
        fcs = [set() for _ in range(n)]
        for i, f in enumerate(favoriteCompanies):
            for name in f:
                if name not in companyMap:
                    companyMap[name] = len(companyMap)
                fcs[i].add(companyMap[name])
        subset = set()
        for i in range(n):
            if i in subset:
                continue
            for j in range(i + 1, n):
                if j in subset:
                    continue
                if fcs[i].issubset(fcs[j]):
                    subset.add(i)
                    break
                if fcs[j].issubset(fcs[i]):
                    subset.add(j)
        return list(filter(lambda x: x not in subset, range(n)))


s = Solution()
print(s.peopleIndexes([["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]))
print(s.peopleIndexes([["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]))
print(s.peopleIndexes([["leetcode"], ["google"], ["facebook"], ["amazon"]]))

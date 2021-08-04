'''
两个列表的最小索引总和
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
示例 2:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
提示:

两个列表的长度范围都在 [1, 1000]内。
两个列表中的字符串的长度将在[1，30]的范围内。
下标从0开始，到列表的长度减1。
两个列表都没有重复的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：哈希
1. 将list1中的餐厅名、索引加入哈希表hashmap
2. 遍历list2，
> 如果当前餐厅list2[i]在hashmap中存在，将hashmap[list2[i]]+i与已保存的最小索引和对比，如果等于，添加；如果小于，清空已保存列表，保存；如果大于忽略
> 如果不存在，跳过

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        for i, name in enumerate(list1):
            hashmap[name] = i
        ans, minIdx = [], float('inf')
        for i, name in enumerate(list2):
            if name in hashmap:
                idx = i + hashmap[name]
                if idx < minIdx:
                    minIdx = idx
                    ans.clear()
                    ans.append(name)
                elif idx == minIdx:
                    ans.append(name)
        return ans

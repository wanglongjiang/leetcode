'''
2023. 连接后等于目标字符串的字符串对
给你一个 数字 字符串数组 nums 和一个 数字 字符串 target ，请你返回 nums[i] + nums[j]（两个字符串连接）
结果等于 target 的下标 (i, j) （需满足 i != j）的数目。



示例 1：

输入：nums = ["777","7","77","77"], target = "7777"
输出：4
解释：符合要求的下标对包括：
- (0, 1)："777" + "7"
- (1, 0)："7" + "777"
- (2, 3)："77" + "77"
- (3, 2)："77" + "77"
示例 2：

输入：nums = ["123","4","12","34"], target = "1234"
输出：2
解释：符合要求的下标对包括
- (0, 1)："123" + "4"
- (2, 3)："12" + "34"
示例 3：

输入：nums = ["1","1","1"], target = "11"
输出：6
解释：符合要求的下标对包括
- (0, 1)："1" + "1"
- (1, 0)："1" + "1"
- (0, 2)："1" + "1"
- (2, 0)："1" + "1"
- (1, 2)："1" + "1"
- (2, 1)："1" + "1"


提示：

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] 和 target 只包含数字。
nums[i] 和 target 不含有任何前导 0 。
'''
from typing import List
'''
一题双解：暴力对比 or 字典树

思路一：暴力对比
双重循环组合任意2个字符串，与Target进行对比
时间复杂度：O(mn^2)，m=target.length,n=nums.length
空间复杂度：O(m)

思路二：字典树
设m=target.length
1. 首先将nums中的字符串加入字典树trie
2. 在trie中搜索target，记录截止每个字符在trie中的字符串个数到数组counts中，counts[i]记录截止target[i]的字符串个数
3. 遍历counts，对于counts[i]，如果target[m-i]在trie中存在，那么counts[i]个开头的字符串可以与trie中的字符串构成target
时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if len(nums[i]) + len(nums[j]) == len(target):
                    if nums[i] + nums[j] == target:
                        ans += 1
                    if nums[j] + nums[i] == target:
                        ans += 1
        return ans


s = Solution()
print(s.numOfPairs(nums=["777", "7", "77", "77"], target="7777") == 4)
print(s.numOfPairs(nums=["123", "4", "12", "34"], target="1234") == 2)
print(s.numOfPairs(nums=["1", "1", "1"], target="11") == 6)

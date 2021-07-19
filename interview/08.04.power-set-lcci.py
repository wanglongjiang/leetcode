'''
面试题 08.04. 幂集
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
from typing import List
'''
思路：回溯
从索引0开始，选择当前索引后，当前索引后的元素依次跳过并进行回溯

时间复杂度：O(n!)
空间复杂度：O(n)，除返回数据外，其他还需要O(n)的空间进行递归
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]

        def backtrack(index, li):
            li.append(nums[index])
            ans.append(li.copy())
            for i in range(index + 1, n):
                backtrack(i, li)
            li.pop()

        for i in range(0, n):
            backtrack(i, [])
        return ans


s = Solution()
print(s.subsets([1, 2, 3]))

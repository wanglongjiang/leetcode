'''
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：哈希
遍历依次s，对于每个字符，如果在哈希表中不存在，保存其下标。
如果存在，将其下标修改为-1
最后遍历依次哈希表，找出下标最小的

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i, c in enumerate(s):
            if c in hashmap:
                hashmap[c] = -1
            else:
                hashmap[c] = i
        ans = float('inf')
        for c, i in hashmap.items():
            if i >= 0:
                ans = min(ans, i)
        return -1 if ans == float('inf') else ans


s = Solution()
print(s.firstUniqChar("lovveleettccodde"))

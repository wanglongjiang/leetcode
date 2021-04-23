'''
最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，
子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
nums 中的所有整数 互不相同
'''
from typing import List
'''
思路：排序+树
1、对数组进行排序
2、建立1棵以1为根节点的树，这个树的性质为：每个节点的值为父节点的整数倍即val%parent == 0
3、从左到右遍历数组，每个元素创建为节点，将其添加到树中。
4、遍历树找到最长的路径即为最大的整除子集

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.child = []


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        # 1、排序
        nums.sort()
        # 2、建立树
        root = Node(1)
        nodeMap = {}  # 快速索引节点
        nodeMap[1] = root
        # 3、将数组元素添加到树中
        i = 1
        startWith1 = True
        if nums[0] != 1:
            startWith1 = False
            nums.insert(0, 1)
            n += 1
        while i < n:
            node = Node(nums[i])
            nodeMap[nums[i]] = node
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    nodeMap[nums[j]].child.append(node)
            i += 1
        # 4、遍历树，找到最长的路径
        ans = []
        pathMap = {}

        def dfs(node):
            if node.val in pathMap:
                return pathMap[node.val]
            subpath = []
            for c in node.child:
                path = dfs(c)
                if len(path) > len(subpath):
                    subpath = path
            path = [node.val]
            path.extend(subpath)
            pathMap[node.val] = path
            return path

        ans = dfs(root)
        if not ans:
            return ans
        if startWith1:
            return ans
        else:  # 如果第1个元素不是1，哨兵1需要排除
            return ans[1:]


s = Solution()
print(
    s.largestDivisibleSubset([
        1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608,
        16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824
    ]))
print(s.largestDivisibleSubset([4, 8, 10, 240]))
print(s.largestDivisibleSubset([2, 4]))
print(s.largestDivisibleSubset(nums=[1, 2, 3]))
print(s.largestDivisibleSubset(nums=[1, 2, 4, 8]))

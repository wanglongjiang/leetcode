'''
与数组中元素的最大异或值

给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。

第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，
其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。

返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。

 

示例 1：

输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
输出：[3,3,7]
解释：
1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

示例 2：

输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
输出：[15,-1,5]
 

提示：

1 <= nums.length, queries.length <= 10^5
queries[i].length == 2
0 <= nums[j], xi, mi <= 10^9

'''
from typing import List
'''
思路：排序+位运算+字典树
求异或最大值应该从最高位开始对比，高位如果有不同的值，超过低位的所有努力。
可以先对queries和nums进行排序，然后每遍历到一个查询时，将nums中<=q[mi]的元素加入字典树，再查询字典树中最高位与q[x]不同的数。
具体算法如下：
1. 对queries每个元素内添加1个原索引（目的是为了将计算结果设置到ans的正确位置上），然后对queries进行排序，排序的key是q[i][m]，也就是下标1的值
2. 对nums进行排序。目的是当查询进行到q[i]时，将所有<=q[i][m]的数加入字典数
3. 遍历queries
    > 先将nums中<=m的整数加入字典树
    >> 字典树的每个节点是一个大小为2的数组，如整数3的二进制是0000 0000 0000 0000 0000 0000 0000 0011，它在字典树中前面30个0会一直选择节点的0下标，最后2个1会选择最后2个节点的下标1
    >> 字典树的第32个节点存放整数

    > 查询字典树中与q[x]高位不同的数，如果找到，将其与q[i][0]进行异或，结果设置到ans中q[i][2]指定的下标处。
    >> 查询字典树，从高位到低位，优先选与目标bit相反的节点，如果与目标bit相反的节点找不到才选择相同的节点，如果全都找不到，返回-1

时间复杂度：O(nlogn)，排序需要O(nLogn)，查询字典树最坏需要O(32logn)
空间复杂度：O(n)
'''


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        for i in range(n):
            queries[i].append(i)
        queries.sort(key=lambda q: q[1])  # 按照q[m]进行排序
        nums.sort(reverse=True)  # 数组进行排序
        trie = [None, None]  # 字典树，下标即为待查询整数的bit

        # 将整数加入trie
        def add(node, bitNum, num):
            bit = ((1 << bitNum) & num) >> bitNum
            if bitNum == 0:
                node[bit] = num
            else:
                if not node[bit]:
                    node[bit] = [None, None]
                add(node[bit], bitNum - 1, num)

        # 查询高位不同于num的数
        def lookup(node, bitNum, num):
            bit = ((1 << bitNum) & ~num) >> bitNum  # 与num相反的位
            if bitNum == 0:
                if node[bit] is not None:  # 优先返回位相异的
                    return node[bit]
                bit = ((1 << bitNum) & num) >> bitNum
                if node[bit] is not None:  # 次选位相同的
                    return node[bit]
                return -1
            if not node[bit]:  # 高位未找到，继续向低位查找
                bit = ((1 << bitNum) & num) >> bitNum
                if not node[bit]:  # 与num位相同的数没有，返回-1
                    return -1
                return lookup(node[bit], bitNum - 1, num)  # 高位与num相同，继续向低位查找
            else:
                return lookup(node[bit], bitNum - 1, num)  # 高位找到了，继续查找

        ans = [0] * n
        # 遍历所有查询
        for q in queries:
            # 将所有<=m的整数加入字典树
            while nums and nums[-1] <= q[1]:
                add(trie, 31, nums.pop())
            # 查询字典树中与q[x]高位不同的数
            num = lookup(trie, 31, q[0])
            if num >= 0:
                ans[q[2]] = num ^ q[0]
            else:
                ans[q[2]] = -1
        return ans


s = Solution()
print(s.maximizeXor(nums=[0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]]))
print(s.maximizeXor(nums=[5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]]))

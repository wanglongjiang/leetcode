'''
翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
'''
from typing import List
'''
思路1，暴力搜索
从第1个开始，搜索后续每个nums[i]>2*nums[j]，需要2重循环
时间复杂度：O(n^2)
空间复杂度：O(1)

思路2，最小堆
从右向左建立最小堆，在建堆过程中查找堆中小于nums[i]/2的值的数量
时间复杂度：建堆需要O(nlogn)，查找过程需要使用dfs，最坏情况下是O(n^2)

思路3，线段树
1、对输入的副本进行排序
2、建立线段树，最底层一共n+1个节点
3、从右向左遍历输入，先查询<nums[i]/2的数字个数，然后将当前元素更新到线段树上
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Node:
    def __init__(self, num, left, right):
        self.count = num
        self.left = left
        self.right = right
        self.lc = None
        self.rc = None


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        union = set()
        newnums = []
        maxval, minval = float('-inf'), float('inf')
        for num in nums:
            if num not in union:
                newnums.append(num)
                union.add(num)
                maxval = max(maxval, num)
                minval = min(minval, num)
        newnums.sort()  # 排序
        n = len(newnums)
        import collections
        q1 = collections.deque()
        # 设置最底层区间
        q1.append(Node(0, newnums[0], newnums[0]))
        for i in range(1, n):
            q1.append(Node(0, newnums[i - 1] + 1, newnums[i]))
        q2 = collections.deque()
        root = None
        # 设置上层区间
        while q1 or q2:
            if not q1 and q2:
                q1, q2 = q2, q1
                continue
            left = q1.popleft()
            right = q1.popleft() if q1 else left
            if left == right and not q2:  # 2个队列中只有1个节点，已经找到根节点
                root = left
                break
            node = Node(0, left.left, right.right)
            node.lc = left
            node.rc = right if left != right else None
            q2.append(node)

        # 定义线段树区间更新函数
        def update(node, left, right):
            if node.right < left or node.left > right:  # 区间不相交
                return
            node.count += 1
            if node.left >= left and node.right <= right:  # 区间被完全包含在目标区间内
                return
            if node.lc and node.lc.right >= left:  # 左子树包含部分区间
                update(node.lc, left, right)
            if node.rc and node.rc.left <= right:  # 右子树包含部分区间
                update(node.rc, left, right)

        # 定义线段树查询函数
        def search(node, left, right):
            if node.right < left or node.left > right:  # 区间不相交
                return 0
            if node.left >= left and node.right <= right:  # 区间被完全包含在目标区间内
                return node.count
            count = 0
            if node.lc and node.lc.right >= left:  # 左子树包含部分区间
                count += search(node.lc, left, right)
            if node.rc and node.rc.left <= right:  # 右子树包含部分区间
                count += search(node.rc, left, right)
            return count

        ans = 0
        # 从右向左遍历输入，先查询<nums[i]/2的数字个数，然后将当前元素更新到线段树上
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            target = (num >> 1) - 1 + (num & 1)  # 目标值为<nums[i]/2的第1个整数
            ans += search(root, minval, target)  # 查询区间minval-nums[i]/2
            update(root, num, num)  # 更新区间minval..num
        return ans


s = Solution()
print(s.reversePairs([5, 4, 3, 2, 1]))
print(s.reversePairs([2, 4, 3, 5, 1]))
print(s.reversePairs([1, 3, 2, 3, 1]))
print(s.reversePairs([2, 4, 3, 5, 1]))

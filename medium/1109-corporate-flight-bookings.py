'''
航班预订统计
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 
意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

提示：

1 <= n <= 2 * 10^4
1 <= bookings.length <= 2 * 10^4
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
'''
from typing import List
'''
思路1，线段树
线段树的区间更新和单点查询
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Node:
    def __init__(self, num, left, right):
        self.num = num
        self.left = left
        self.right = right


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        tree = [None] * 4 * n

        # 建树
        def build(i, left, right):
            tree[i] = Node(0, left, right)
            if left == right:
                return
            mid = (left + right) // 2
            build(2 * i, left, mid)
            build(2 * i + 1, mid + 1, right)

        build(1, 1, n)

        # 区间更新
        def update(i, left, right, val):
            if tree[i].left >= left and tree[i].right <= right:  # 区间被完全包含在目标区间内
                tree[i].num += val
                return
            if tree[i * 2].right >= left:  # 左子树包含部分区间
                update(i * 2, left, right, val)
            if tree[i * 2 + 1].left <= right:  # 右子树包含部分区间
                update(i * 2 + 1, left, right, val)

        # 单点查询
        def search(i, target, ans):
            ans += tree[i].num  # 进行累加
            if tree[i].left == tree[i].right:  # 已找到叶子节点，返回
                return ans
            if target <= tree[i * 2].right:
                return search(i * 2, target, ans)
            if target >= tree[i * 2 + 1].left:
                return search(i * 2 + 1, target, ans)

        # 遍历输入，进行区间更新
        for item in bookings:
            update(1, item[0], item[1], item[2])
        # 输出结果
        ans = [0] * n
        for i in range(n):
            ans[i] = search(1, i + 1, 0)
        return ans


s = Solution()
print(s.corpFlightBookings([[5, 6, 45], [5, 6, 5], [1, 6, 10], [5, 6, 5], [1, 2, 15], [1, 2, 5]], 6))
print(s.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
print(s.corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2))

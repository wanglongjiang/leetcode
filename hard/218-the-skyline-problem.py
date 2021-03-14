'''
天际线问题
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。
此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
'''
from typing import List
'''
思路：单调栈
把楼的左上角看成入栈，右上角看成出栈。
    入栈时观察栈顶元素高度是否大于当前元素高度，
        如果栈顶元素大于当前元素，天际线不会变化，但因为本元素可能会对后续的天际线造成影响，需要将本元素插入栈中相应的位置。
        如果栈顶元素等于当前元素，天际线不会变化，当前元素入栈。
        如果栈顶元素小于当前元素，需要将本元素入栈到栈顶，天际线升高为栈顶元素。
    出栈时观察栈顶元素，
        如果栈顶元素大于当前元素，天际线没有变化，从栈中找到该元素相同高度的入栈高度，清零（清零的原因是暂时不出栈，提高性能）
        如果栈顶元素等于当前元素，当前元素出栈，天际线降低为新的栈顶元素
        如果栈顶元素为0，直接抛弃
具体算法为：
1、将输入提取出右上角x,y坐标，形成列表rightList，内部元素按照x坐标升序排序
2、同时读取buildings和rightList，哪个列表的第1个元素的x坐标小，先读取哪个元素。
    从building中读取的元素高度用作入栈，从rightList中读取的元素用于出栈。
    入栈出栈的算法见上面文字。出入栈的过程中如果天际线发生变化，将变化输出结果中。
时间复杂度：需要提取出rightList并排序,平均情况下O(nlogn)，
    最坏情况下O(n^2)，最坏情况指所有的楼形成嵌套结构，第1个楼在最外面，最后1个楼嵌套在最内部。
空间复杂度：O(n)，需要1个辅助数组。
'''


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        # 提取出buildings元素item中的右坐标、高度
        rightList = list(sorted(map(lambda item: (item[1], item[2]), buildings), key=lambda item: item[0]))
        i, j = 0, 0
        ans, stack = [], []

        # 入栈操作
        def push(item):
            if not stack or item[2] > stack[-1]:  # 高于栈顶元素，天际线升高
                ans.append([item[0], item[2]])
                stack.append(item[2])
            elif stack[-1] == item[2]:  # 高度相同，天际线无变化
                stack.append(item[2])
            else:  # 低于栈顶元素，天际线无变化，需要找到应该在的位置，插入
                # 这里可以进行优化，当前入栈的高度已经低于栈顶高度，如果出栈队列中直至该高度出栈，都低于该高度，
                # 说明当前楼的轮廓不会出现在天际线里，可以直接抛弃，不需要入栈
                if rightList[j][1] == item[2]:
                    del rightList[j]
                    return
                # 不能优化，继续执行
                k = len(stack) - 1
                while k >= 0 and (stack[k] > item[2] or not stack[k]):
                    k -= 1
                stack.insert(k + 1, item[2])

        # 出栈操作
        def pop(item):
            while stack and not stack[-1]:  # 清除栈顶的0
                stack.pop()
            if stack[-1] == item[1]:  # 高度与栈顶元素相同，观察栈内下一个元素高度是否降低
                stack.pop()
                while stack and not stack[-1]:  # 清除栈顶的0
                    stack.pop()
                if not stack:  # 栈为空，高度降为0
                    ans.append([item[0], 0])
                elif stack[-1] < item[1]:  # 栈不为空，高度降为新的栈顶
                    ans.append([item[0], stack[-1]])
                else:  # 新的栈顶高度与出栈高度相同，高度无变化
                    pass
            else:  # 高度低于栈顶元素，从栈中找到该元素相同高度的入栈高度，清零（清零的原因是暂时不出栈，提高性能）
                k = len(stack) - 1
                while stack[k] != item[1]:  # 栈中肯定能找到相同高度的元素
                    k -= 1
                stack[k] = 0

        # 读取building和rightList，执行入出栈操作
        while i < n and j < len(rightList):
            pushItem, popItem = buildings[i], rightList[j]
            if pushItem[0] <= popItem[0]:
                push(pushItem)
                i += 1
            else:
                pop(popItem)
                j += 1
        while j < n:
            pop(rightList[j])
            j += 1

        return ans


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline([[0, 2, 3], [2, 5, 3]]))

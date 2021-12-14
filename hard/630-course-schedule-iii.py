'''
630. 课程表 III
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 
表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。

 

示例 1：

输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
示例 2：

输入：courses = [[1,2]]
输出：1
示例 3：

输入：courses = [[3,2],[4,3]]
输出：0
 

提示:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104
'''
from typing import List
import heapq
'''
思路：贪心 堆
1. 对课程按照完成时间从小到大排序
2. 设置一个最大堆，用于保存所有选中的课程；设置一个变量totalTime，保存所有已选中课程的总课时
3. 迭代课程，对于每个课程，
    如果它的课时+totalTime<=它自身的lastDayi，这门课可以上，加入堆；
    如果它的课时+totalTime>它自身的lastDayi，如果小于堆中的最长的课程，可以替换掉最大的课程，否则将抛弃该课程

时间复杂度：O(nlogn)，排序、加入堆都需要O(nlogn)时间
空间复杂度：O(n)
'''


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])  # 按照最晚完成时间排序
        heap = []
        totalTime = 0
        for c in courses:
            if c[0] + totalTime <= c[1]:  # 当前课程+已选课总课时<=最后截止日，可以选课
                heapq.heappush(heap, -c[0])  # 该课程被选中，加入堆
                totalTime += c[0]  # 累加总课时
            elif heap and c[0] < -heap[0]:  # 当前课程不能直接选中，需要剔除一个已有课程。如果当前课时小于已有最大课时，可以加入，否则不划算，不加入
                totalTime = totalTime + heapq.heapreplace(heap, -c[0]) + c[0]
        return len(heap)


s = Solution()
print(s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(s.scheduleCourse([[1, 2]]))
print(s.scheduleCourse([[3, 2], [4, 3]]))

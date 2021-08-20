'''
剑指 Offer II 113. 课程顺序
现在总共有 numCourses 门课需要选，记为 0 到 numCourses-1。

给定一个数组 prerequisites ，它的每一个元素 prerequisites[i] 表示两门课程之间的先修顺序。
例如 prerequisites[i] = [ai, bi] 表示想要学习课程 ai ，需要先完成课程 bi 。

请根据给出的总课程数  numCourses 和表示先修顺序的 prerequisites 得出一个可行的修课序列。

可能会有多个正确的顺序，只要任意返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

 

示例 1:

输入: numCourses = 2, prerequisites = [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
示例 3:

输入: numCourses = 1, prerequisites = []
输出: [0]
解释: 总共 1 门课，直接修第一门课就可。
 

提示:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
prerequisites 中不存在重复元素
 

注意：本题与主站 210 题相同：https://leetcode-cn.com/problems/course-schedule-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/QA2IGt
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：拓扑排序
使用队列、入度数组进行拓扑排序
时间复杂度：O(n)，创建入度数组，遍历所有节点
空间复杂度：O(n)，需要入度数组，队列，后续课程哈希表，最坏情况下大小都是n
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        import collections
        indegree = [0] * numCourses  # 入度
        edge = [[] for _ in range(numCourses)]  # 后续课程邻接表
        # 遍历依赖关系，生成入度，邻接表
        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            edge[prereq[1]].append(prereq[0])
        queue = collections.deque()
        # 将入度为0的课程加入队列
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
        # BFS遍历课程，将队列中的课程加入结果，将课程的后续课程入度-1，如果后续课程的入度变成0，加入队列进行遍历
        ans = []
        while queue:
            c = queue.popleft()
            ans.append(c)
            for next in edge[c]:  # 遍历该课程的后续
                indegree[next] -= 1  # 后续课程的入度-1
                if indegree[next] == 0:  # 如果后续课程的入度变成0，加入队列
                    queue.append(next)
        if len(ans) == numCourses:
            return ans
        else:
            return []

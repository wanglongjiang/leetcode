-- 有一个courses 表 ，有: student (学生) 和 class (课程)。
-- 请列出所有超过或等于5名学生的课。

-- 思路：简单的分组
select class
from courses
group by class
having count(*)>=5
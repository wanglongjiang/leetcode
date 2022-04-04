 # 上升的温度 # 编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 id 。
select t1.id as id
from Weather t1,Weather t2
where DATEDIFF(t1.recordDate, t2.recordDate) = 1
and t1.Temperature>t2.Temperature
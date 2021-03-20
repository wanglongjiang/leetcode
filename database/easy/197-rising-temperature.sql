 # 上升的温度 # 编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 id 。
SELECT  t1.id AS id
FROM Weather t1,Weather t2
WHERE t1.RecordDate=t2.RecordDate+1 
AND t1.Temperature>t2.Temperature 
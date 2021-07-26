-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。
SELECT
	DISTINCT t2.num AS ConsecutiveNums 
FROM
	LOGS t1,
	LOGS t2,
	LOGS t3 
WHERE
	t1.id = t2.id + 1 
	AND t2.id = t3.id + 1 
	AND t1.num = t2.num 
	AND t2.num = t3.num

# 删除重复的电子邮箱
# 编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。

# 因垂丝汀，mysql删除的where条件里面的表名不能直接保留到where条件里，需要外包一层
 delete
FROM Person
WHERE id not in( 
SELECT  id
FROM 
(
	SELECT  MIN(id)as id
	FROM person
	GROUP BY  email 
)t) 
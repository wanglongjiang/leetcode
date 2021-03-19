 # 从不订购的客户 某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。
SELECT  name AS Customers
FROM 
(
	SELECT  name 
	       ,o.id
	FROM customers c
	LEFT JOIN orders o
	ON c.id=o.customerId 
) t
WHERE id is null  
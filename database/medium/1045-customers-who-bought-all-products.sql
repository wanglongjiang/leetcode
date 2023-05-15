SELECT
	customer_id 
FROM
	( SELECT customer_id, count( * ) AS c_count FROM Customer GROUP BY customer_id ) c,
	( SELECT count( * ) AS all_count FROM Product ) p 
WHERE
	c_count = all_count
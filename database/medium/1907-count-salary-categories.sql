SELECT
	m.category,
	ifnull( t.count, 0 ) AS accounts_count 
FROM
	( SELECT 'Low Salary' category UNION SELECT 'Average Salary' UNION SELECT 'High Salary' ) m
	LEFT JOIN (
	SELECT
		category,
		count( * ) count 
	FROM
		( SELECT CASE WHEN income < 20000 THEN 'Low Salary' WHEN income > 50000 THEN 'High Salary' ELSE 'Average Salary' END AS category FROM Accounts ) t0 
	GROUP BY
	category 
	) t ON m.category = t.category
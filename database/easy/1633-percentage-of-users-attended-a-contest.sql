SELECT
	r.contest_id,
	round( count( r.user_id ) * 100 / total, 2 ) AS percentage 
FROM
	register r,
	( SELECT count( * ) AS total FROM USERS ) u 
GROUP BY
	r.contest_id 
ORDER BY
	percentage DESC,
	contest_id
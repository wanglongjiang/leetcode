SELECT
	round( count( b.event_date ) / count( a.player_id ), 2 ) AS fraction 
FROM
	( SELECT player_id, min( event_date ) AS event_date FROM Activity GROUP BY player_id ) a
	LEFT JOIN Activity b ON a.player_id = b.player_id 
	AND a.event_date = date_add( b.event_date, INTERVAL -1 DAY )
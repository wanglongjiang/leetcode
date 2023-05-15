SELECT
	product_id,
	round( sum( amount ) / sum( units ), 2 ) AS average_price 
FROM
	(
	SELECT
		p.product_id,
		u.units,
		p.price * u.units AS amount 
	FROM
		prices p,
		unitssold u 
	WHERE
		p.product_id = u.product_id 
		AND p.start_date <= u.purchase_date AND p.end_date >= u.purchase_date 
	) t 
GROUP BY
	p.product_id
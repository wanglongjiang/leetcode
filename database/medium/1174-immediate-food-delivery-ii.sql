SELECT
	round( count( d.customer_id ) * 100 / count( t.customer_id ), 2 ) AS immediate_percentage
FROM
	(
	SELECT
		customer_id,
		min( order_date ) as min_date
	FROM
		delivery
	GROUP BY
	customer_id 
	) t
left join 
    (SELECT customer_id,customer_pref_delivery_date from delivery WHERE customer_pref_delivery_date=order_date) d
    on t.customer_id = d.customer_id and t.min_date = d.customer_pref_delivery_date

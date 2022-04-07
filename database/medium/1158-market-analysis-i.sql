select u.user_id as buyer_id,join_date,ifnull(orders_in_2019,0) as orders_in_2019
from users u
left join 
(select buyer_id,count(1) as orders_in_2019 
from orders o
where year(order_date)='2019'
group by buyer_id) o
on u.user_id = o.buyer_id

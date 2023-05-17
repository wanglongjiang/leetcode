select t.product_id,ifnull(new_price,10) as price
from
(select distinct product_id
from products) t
left join 
(select t2.product_id,t2.new_price
from
products t2,
(select product_id,max(change_date) as max_date
from products
where change_date<='2019-08-16'
group by product_id) t3
where t2.product_id = t3.product_id and t3.max_date=t2.change_date) t0
on t.product_id = t0.product_id

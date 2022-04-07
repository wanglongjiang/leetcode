select t1.stock_name,t2.price-t1.price as capital_gain_loss 
from(
select stock_name,sum(price) as price
from stocks
where operation='Buy'
group by stock_name)t1,
(
select stock_name,sum(price) as price
from stocks
where operation='Sell'
group by stock_name)t2
where t1.stock_name=t2.stock_name

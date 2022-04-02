-- 进店却未进行过交易的顾客
select customer_id ,count(1) as count_no_trans 
from Visits v
where not exists(select 1 from Transactions t where t.visit_id =v.visit_id )
group by customer_id
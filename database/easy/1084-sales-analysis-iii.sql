select distinct p.product_id,product_name
from Product p,Sales s
where p.product_id=s.product_id
and s.sale_date between str_to_date('2019-01-01','%Y-%m-%d') and str_to_date('2019-03-31','%Y-%m-%d')
and not exists(select 1 from Sales s1 where p.product_id=s1.product_id 
and (sale_date<str_to_date('2019-01-01','%Y-%m-%d') or sale_date>str_to_date('2019-03-31','%Y-%m-%d')))

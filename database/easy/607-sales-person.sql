-- 销售员
select s.name
from SalesPerson s
where not exists(select 1 from company c,orders o where c.com_id=o.com_id and c.name='RED' and s.sales_id=o.sales_id)

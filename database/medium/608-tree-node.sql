# 树节点

select id,case when p_id is null then 'Root' when not exists(select 1 from tree t2 where t.id=t2.p_id) then 'Leaf' else 'Inner' end as type
from tree t
order by id

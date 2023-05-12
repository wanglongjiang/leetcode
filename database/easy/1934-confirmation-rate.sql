select s.user_id,round(ifnull(confirmation_rate ,0),2) as confirmation_rate
from Signups s
left join (
    select user_id,sum(case action when 'confirmed' then 1 else 0 end) / count(1) as confirmation_rate
    from Confirmations
    group by user_id
) c on s.user_id = c.user_id
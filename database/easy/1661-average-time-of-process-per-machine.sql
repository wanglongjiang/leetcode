select machine_id,round(sum(processing_time)/count(process_id),3) as processing_time
from(
select a1.machine_id,a1.process_id,(a2.timestamp - a1.timestamp) as processing_time
from Activity a1,Activity a2
where a1.activity_type ='start' and a2.activity_type ='end' and a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
) t
group by machine_id

select s.student_id ,s.student_name ,s.subject_name,count(e.subject_name) as attended_exams 
from 
(select student_id ,student_name ,subject_name 
from Students s,Subjects sub
) s
left join Examinations e on s.student_id = e.student_id and s.subject_name=e.subject_name
group by student_id ,student_name ,subject_name
order by student_id ,subject_name
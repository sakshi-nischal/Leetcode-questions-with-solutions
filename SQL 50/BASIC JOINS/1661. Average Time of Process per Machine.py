# Write your MySQL query statement below

select e.machine_id, round(avg(e.timestamp - s.timestamp),3) as processing_time
from activity as e, activity as s
where e.machine_id = s.machine_id and e.process_id = s.process_id and e.activity_type = "end" and s.activity_type = "start"
group by e.machine_id


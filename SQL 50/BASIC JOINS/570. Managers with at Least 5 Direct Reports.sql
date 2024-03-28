# Write your MySQL query statement below

select e.name
from employee e join employee emp
on e.id = emp.managerid
group by emp.managerid having count(emp.managerid) >= 5

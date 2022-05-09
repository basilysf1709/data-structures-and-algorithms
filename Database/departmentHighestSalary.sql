select d.name as Department,e.name as Employee ,e.salary as Salary from Employee e INNER join Department d 
on e.departmentid=d.id where e.salary=(select max(salary) from Employee e2 where e.departmentid=e2.departmentid group by departmentid)
-- Check this
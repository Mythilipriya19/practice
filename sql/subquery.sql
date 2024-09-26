
--subquery

use company


create table student(


id int PRIMARY KEY,

name varchar(20),

email varchar(30) UNIQUE,

age int NOT NULL,

class int DEFAULT 10

)


INSERT INTO student (id,name,email,age) VALUES (1,'Rex','rex2@mail.com',20),
(2,'mythili','mex@mail.com',50),
(4,'anu','aex@mail.com',70),
(5,'aruna','rex@mail.com',30),
(6,'priya','rex1@mail.com',60)

select * from student

--view

create view my     
as
select * from student where age in (select age from student where age > 20);

select * from my;

--aggregation

select * from student where age in (select sum(age) from student)

----groupby

select  id,sum(age) from student group by id 


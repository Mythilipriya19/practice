--joins
create database company;

create table department(

id int,

dprt varchar(20)

)
create table worker(

id int,

name varchar(20)

)


insert into worker VALUES(1,'mythili'),
(2,'priya'),(3,'anu');

insert into department VALUES(1,'eng'),
(2,'tamil'),(4,'maths');


select * from worker;

select * from department;

create view acc
as
select worker.id , worker.name ,department.dprt from worker RIGHT JOIN department ON worker.id = department.id           --right join

select * from acc;

--union

select * from worker union select * from department;

--union all

select * from worker union all select * from department;
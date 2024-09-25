--window functions:

create database school

create table studentt(
id int,
name varchar(20),
maths int,
tamil int,
eng int,
total int
);

insert into studentt VALUES (1,'mythili',90,30,20,400),
(2,'priya',80,20,20,350),
(3,'anu',90,30,40,400),
(4,'aruna',90,20,30,400),
(5,'dharu',80,50,40,304),
(6,'kalai',90,30,20,299),
(7,'kevin',90,30,20,307);


select * from studentt;

--ROW_NUMBER()

select ROW_NUMBER() OVER(PARTITION BY maths ORDER BY total DESC) rn
id,
name,
maths,
tamil,
eng,
total,

select * from studentt;

--RANK()

select Rank() OVER(PARTITION BY maths ORDER BY total DESC) rn
id,
name,
maths,
tamil,
eng,
total,

select * from studentt;

--DENSE_RANK()

select Dense_rank() OVER(PARTITION BY maths ORDER BY total DESC) rn
id,
name,
maths,
tamil,
eng,
total,

select * from studentt;

